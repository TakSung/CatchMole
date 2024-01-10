from abc import *
from typing import List
from Common.ObjectType import *
from Domain.Interfaces.IRaiseObj import IRaiseObj


class IBoard(metaclass=ABCMeta):
    ## 현재 보드 상태 전부 보여준다.
    @abstractmethod
    def get_board_state(self) -> List[List[ObjectType]]:
        pass

    @abstractmethod
    def get_state(self, y: int, x: int) -> ObjectType:
        pass

    @abstractmethod
    def raise_obj(self, y: int, x: int, type: ObjectType) -> IRaiseObj:
        pass

    def set_obj(self, y: int, x: int, obj: IRaiseObj) -> IRaiseObj:
        pass

    @abstractmethod
    def try_attack(self, y: int, x: int) -> ObjectType:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass
