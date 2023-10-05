from abc import *
from Common.ObjectType import *


class IBoard(metaclass=ABCMeta):
    @abstractmethod
    def get_state(self, y: int, x: int) -> ObjectType:
        pass

    @abstractmethod
    def raise_mole(self, y: int, x: int, type: ObjectType) -> None:
        pass
