from json import load, dump, dumps, loads
from logging import getLogger

import falcon

from src.domain.ports.input.controller import Controller
from src.domain.ports.input.registry_vote import RegistryVote
from src.domain.entities.vote import Vote


class VoteController(Controller):
    
    def __init__(self, service: RegistryVote, *args, **kwargs):
        self.service: RegistryVote = service
        self.logger = getLogger('app')
    
    def on_get_vote(self, req, resp, code=None):
        self.logger.debug("Handling a get request")
        vote = self.service.get_vote(code=code)
        
        resp.set_header('Powered-By', 'Falcon')
        
        if vote:
            resp.text = vote.json()
            resp.status = falcon.HTTP_200
            return
        
        resp.status = falcon.HTTP_404
        resp.text = dumps({
            "message": f"Vote option with code {code} not found.",
            "status": falcon.HTTP_404
        })
    
    def on_post(self, req, resp):
        # TODO: handle if code doesn't exist.
        body: dict = loads(req.stream.peek())
        code = body.get('code')
        
        if not code:
            raise
        
        self.service.save_vote(code=code)
        
        resp.status = falcon.HTTP_200
        resp.text = dumps({
            "message": f"Vote {code} saved successfully!",
            "status": falcon.HTTP_200
        })
        
    def on_put(self, req, resp):
        # TODO: handle if code already exists.
        body: dict = loads(req.stream.peek())
        code = body.get('code')
        
        if not code:
            raise
        
        self.service.create_vote_option(code=code)
        
        resp.status = falcon.HTTP_200
        resp.text = dumps({
            "message": f"Vote option {code} created successfully!",
            "status": falcon.HTTP_200
        })


    
    def on_delete(self, req, resp):
        pass