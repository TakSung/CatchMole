import __init__
from abc import *
from typing import Tuple
from Common import ObjectType, PlayerState


class IConvertObjectToState(metaclass=ABCMeta):
    @abstractclassmethod
    def convert(y:int, x:int, type:ObjectType)-> Tuple[PlayerState, float]:
        ...