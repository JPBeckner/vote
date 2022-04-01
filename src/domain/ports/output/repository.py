import abc
from typing import List

from src.domain.entities import Vote


class Repository(metaclass=abc.ABCMeta):
    """
    Interface. Output port to connect to the database.
    """
    
    @abc.abstractmethod
    def save_vote(self, vote: Vote):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_vote(self, code: int) -> Vote:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_all_votes(self) -> List[Vote]:
        raise NotImplementedError
    