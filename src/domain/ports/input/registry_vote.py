import abc

from src.domain.entities import Vote


class RegistryVote(metaclass=abc.ABCMeta):
    
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            (
                hasattr(subclass, 'save_vote') and
                callable(subclass.save_vote)
            ) and (
                hasattr(subclass, 'get_vote') and
                callable(subclass.get_vote)
            ) or
            NotImplemented
        )

        
    @abc.abstractmethod
    def save_vote(self, vote: Vote):
        raise NotImplementedError
    
    @abc.abstractmethod
    def create_vote_option(self, code: int):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_vote(self, code: int) -> Vote:
        raise NotImplementedError
