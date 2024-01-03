import __init__
from typing import Tuple

from Common import ObjectType, PlayerState
from Application.StateFilter import IConvertObjectToState


class BuffFilter(IConvertObjectToState):
    def convert(self, y: int, x: int, type: ObjectType) -> Tuple[PlayerState, float]:
        match type:
            case _:
                return (PlayerState.Nomal, 0)


class DebuffFilter(IConvertObjectToState):
    def __init__(self, time: float = 3.0):
        self.time = time

    def convert(self, y: int, x: int, type: ObjectType) -> Tuple[PlayerState, float]:
        match type:
            case ObjectType.BASIC_MOLE:
                return (PlayerState.Reverse, self.time)
            case _:
                return (PlayerState.Nomal, 0)
