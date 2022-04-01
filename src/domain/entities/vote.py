

class Vote:
    
    def __init__(
        self,
        code: int,
        count: int,
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
