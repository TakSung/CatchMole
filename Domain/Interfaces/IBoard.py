from abc import *
from Common.ObjectType import *
from Domain.Interfaces.IRaiseObj import IRaiseObj


class IBoard(metaclass=ABCMeta):
    @abstractmethod
    def get_state(self, y: int, x: int) -> ObjectType:
        pass

    @abstractmethod
    def raise_obj(self, y: int, x: int, type: ObjectType) -> IRaiseObj:
        pass
