import __init__
from abc import *
from typing import Tuple
from Common import ObjectType, PlayerState


class IConvertObjectToState(metaclass=ABCMeta):
    @abstractclassmethod
    def convert(self, y: int, x: int, type: ObjectType) -> Tuple[PlayerState, float]:
        """_summary_

        Args
            y (int): _description_
            x (int): _description_
            type (ObjectType): _description_

        Returns:
            Tuple[PlayerState, float]: _description_ (상태관련 정보, 유지시간(0이면 실행안됨))
        """
        ...
