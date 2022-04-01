import abc

from peewee import Database
from falcon import Request, Response


class Controller(metaclass=abc.ABCMeta):
    
    db: Database
    
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            (
                hasattr(subclass, 'on_get') and
                callable(subclass.on_get)
            ) and (
                hasattr(subclass, 'on_post') and
                callable(subclass.on_post)
            ) and (
                hasattr(subclass, 'on_delete') and
                callable(subclass.on_delete)
            ) or
            NotImplemented
        )

    
    @abc.abstractmethod
    def on_get(self, req: Request, resp: Response, code=None):
        raise NotImplementedError
    
    @abc.abstractmethod
    def on_post(self, req: Request, resp: Response):
        raise NotImplementedError
    
    @abc.abstractmethod
    def on_delete(self, req: Request, resp: Response):
        raise NotImplementedError