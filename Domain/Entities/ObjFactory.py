from abc import *
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Interfaces.IMoleObserver import IMoleObserver
from Common.ObjectType import ObjectType

from Domain.Entities.Mole import Mole


class IObjFactory(metaclass=ABCMeta):
    @abstractmethod
    def get_obj(self, y: int, x: int, type: ObjectType, observer: IMoleObserver) -> IRaiseObj:
        pass


class ObjFactory(IObjFactory):
    def get_obj(self, y: int, x: int, type: ObjectType, observer: IMoleObserver) -> IRaiseObj:
        obj = None
        match type:
            case ObjectType.NONE:
                raise Exception('"ObjectType.NONE" 를 입력으로 넣지 말아주세요.')
            case ObjectType.BASIC_MOLE:
                obj = Mole(y, x, observer)
        return obj


class TestObjFactory(IObjFactory):
    def get_obj(self, y: int, x: int, type: ObjectType, observer: IMoleObserver) -> IRaiseObj:
        obj = None
        match type:
            case ObjectType.NONE:
                raise Exception('"ObjectType.NONE" 를 입력으로 넣지 말아주세요.')
            case ObjectType.BASIC_MOLE:
                obj = Mole(y, x, observer, 0.1)
        return obj
