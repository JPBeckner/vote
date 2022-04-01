from typing import List

from src.domain.ports.output import Repository
from src.domain.entities import Vote
from logging import getLogger


class RepositoryImpl(Repository):
    
    def __init__(
        self,
        *args,
        **kwargs
    ):
        self.logger = getLogger('app')
    
    def save_vote(self, vote: Vote):
        pass
    
    def get_vote(self, code: int):
        self.logger.debug('the repo is accepting a vote on de DB')
        return Vote(code=code, count=2022)
    
    def get_all_votes(self) -> List[Vote]:
        pass