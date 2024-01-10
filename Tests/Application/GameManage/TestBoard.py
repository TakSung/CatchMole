from typing import List
from Common.ObjectType import *
from Domain.Interfaces import IRaiseObj, IBoard


class TestHalfHackerBoard(IBoard):
    ## 현재 보드 상태 전부 보여준다.
    def get_board_state(self) -> List[List[ObjectType]]:
        return [[ObjectType.HACKER for x in range(5)] for y in range(5)]

    def get_state(self, y: int, x: int) -> ObjectType:
        return ObjectType.HACKER

    def raise_obj(self, y: int, x: int, type: ObjectType) -> IRaiseObj:
        raise NotImplementedError()

    def set_obj(self, y: int, x: int, obj: IRaiseObj) -> IRaiseObj:
        raise NotImplementedError()

    def try_attack(self, y: int, x: int) -> ObjectType:
        match y:
            case v if v >= 3:
                return ObjectType.HACKER
            case _:
                return ObjectType.BASIC_MOLE

    def get_size(self) -> int:
        return 5
