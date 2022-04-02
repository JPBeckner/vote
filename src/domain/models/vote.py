from peewee import *

from src.domain.models import connection
from src.domain.entities.vote import Vote as VoteEntity


class Vote(Model):  
    
    id = AutoField(primary_key=True)
    code = IntegerField()
    count = IntegerField()
    
    class Meta:
        database = connection
        table_name = "vote"
        
    def from_vote(self, vote: VoteEntity):
        self.code = vote.code
        self.count = vote.count
        
    def get_vote(self):
        return VoteEntity(
            code=self.code,
            count=self.count,
        )
