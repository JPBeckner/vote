# from json import load, dump, dumps, loads
from logging import getLogger

import falcon
from spectree import Response

from src.domain.ports.input.controller import Controller
from src.domain.ports.input.registry_vote import RegistryVote
# from src.domain.entities.vote import Vote
from src.adapter.falcon import spec
from src.adapter.falcon.models.code import Code
from src.adapter.falcon.models.status_message import StatusMessage


class VoteController(Controller):
    
    def __init__(self, service: RegistryVote, *args, **kwargs):
        self.service: RegistryVote = service
        self.logger = getLogger('app')
    
    @spec.validate(tags=('api',))
    def on_get_vote(self, req, resp, code: int):
        """Get an existing vote from the given code.
        """
        self.logger.debug("Handling a get request")
        vote = self.service.get_vote(code=code)
        
        resp.set_header('Powered-By', 'Falcon')
        
        if vote:
            resp.media = vote.to_dict()
            resp.status = falcon.HTTP_200
            return
        
        resp.status = falcon.HTTP_404
        resp.media = {
            "message": f"Vote option with code {code} not found.",
            "status": falcon.HTTP_404
        }
    
    @spec.validate(
        json=Code, 
        resp=Response(
            HTTP_200=StatusMessage,
            HTTP_500=None
        ), 
        tags=('api',)
    )
    def on_put(self, req, resp):
        # TODO: handle if code doesn't exist.
        body: dict = req.media
        code = body.get('code')
        
        if not code:
            raise
        
        self.service.save_vote(code=code)
        
        resp.status = falcon.HTTP_200
        resp.media = {
            "message": f"Vote {code} saved successfully!",
            "status": falcon.HTTP_200
        }

    @spec.validate(tags=('api',))        
    def on_post(self, req, resp):
        # TODO: handle if code already exists.
        
        body: dict = req.media
        code = body.get('code')
        
        if not code:
            raise
        
        self.service.create_vote_option(code=code)
        
        resp.status = falcon.HTTP_200
        resp.media = {
            "message": f"Vote option {code} created successfully!",
            "status": falcon.HTTP_200
        }
    
    @spec.validate(tags=('api',))
    def on_delete(self, req, resp):
        self.logger.debug("on_delete")
        
        body: dict = req.media
        code = body.get('code')
        
        if not code:
            resp.status = falcon.HTTP_400
            resp.media = {
                "message": "A vote code must be specified!",
                "status": falcon.HTTP_400
            }
        
        deleted = self.service.delete_vote(code=body.get('code'))
        
        if deleted:
            msg = f"Vote option {code} deleted successfully!"
            self.logger.info(msg)
            resp.status = falcon.HTTP_200
            resp.media = {
                "message": msg,
                "status": falcon.HTTP_200
            }
            return

        msg = f"Vote option {code} can't be deleted!"
        self.logger.info(msg)
        resp.status = falcon.HTTP_500
        resp.media = {
            "message": msg,
            "status": falcon.HTTP_500
        }
