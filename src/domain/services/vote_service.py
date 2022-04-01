from src.domain.ports.input.registry_vote import RegistryVote
from src.domain.entities import Vote
from src.domain.ports.output import Repository
from logging import getLogger

class RegistryVoteImpl(RegistryVote):
    
    def __init__(
        self,
        repo: Repository,
        *args,
        **kwargs
    ):
        
        # self.vote = vote
        self.repo = repo
        self.logger = getLogger('app')
        
    
    def save_vote(self, vote: Vote):
        self.save_vote(vote=vote)
        
    def get_vote(self, code: int):
        self.logger.debug("the vote service is getting a Vote from de Repo")
        return self.repo.get_vote(code=code)
    
    
    