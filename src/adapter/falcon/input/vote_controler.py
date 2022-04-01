from json import load, dump, dumps
from logging import getLogger

import falcon

from src.domain.ports.input.controller import Controller
from src.domain.ports.input.registry_vote import RegistryVote
from src.domain.entities.vote import Vote


class VoteController(Controller):
    
    def __init__(self, service: RegistryVote, *args, **kwargs):
        self.service: RegistryVote = service
        self.logger = getLogger('app')
    
    def on_get(self, req, resp, code=None):
        self.logger.debug("Handling a get request")
        vote = self.service.get_vote(code=code)
        resp.text = dumps({
            "code": vote.code,
            "count": vote.count,
        })
        resp.set_header('Powered-By', 'Falcon')
        
        resp.status = falcon.HTTP_200
    
    def on_post(self, req, resp):
        body: dict = load(req.stream)
        vote = Vote(**body)
        self.service.save_vote(vote=vote)
    
    def on_delete(self, req, resp):
        pass