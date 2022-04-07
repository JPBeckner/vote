from typing import List
from logging import getLogger

from peewee import *

from src.domain.ports.output import Repository
from src.domain.entities import Vote as VoteEntity
from src.domain.models.vote import Vote as VoteModel


class RepositoryImpl(Repository):
    
    def __init__(
        self,
        db: Database,
        *args,
        **kwargs
    ):
        self.logger = getLogger('app')
    
    def save_vote(self, code: int):
        vote = VoteModel.get(
            VoteModel.code == code
        )
        vote.count += 1
        vote.save()
    
    def create_vote_option(self, code):
        VoteModel.create(
            code=code,
            count=0,
        )
    
    def get_vote(self, code: int):
        self.logger.debug('the repo is accepting a vote on de DB')
        vote: VoteModel = VoteModel.get_or_none(
            VoteModel.code == code
        )
        if vote:
            return vote.get_vote()
        return None
    
    def get_all_votes(self) -> List[VoteEntity]:
        pass
    
    def delete_vote(self, code: int) -> bool:
        return bool(
            VoteModel.delete().where(
                VoteModel.code == code
            ).execute()
        )
