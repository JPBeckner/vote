import json


class Vote:
    
    def __init__(
        self,
        code: int = 0,
        count: int = 0,
        *args,
        **kwargs
    ):
        self.__code = code
        self.__count = count
    
    @property
    def code(self) -> int:
        return self.__code
    
    @property
    def count(self) -> int:
        return self.__count
    
    @count.setter
    def count(self, value):
        self.__count = value
        
    def from_dict(self, dict: dict):
        self.code = dict.get('code', 0)
        self.count = dict.get('count', 0)
        
    def to_dict(self):
        return {
            "code": self.code,
            "count": self.count,
        }
        
    def json(self):
        return json.dumps(self.to_dict())
