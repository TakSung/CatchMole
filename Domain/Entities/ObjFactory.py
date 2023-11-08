from abc import *
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Interfaces.IMoleObserver import IMoleObserver
from Common.ObjectType import ObjectType

from Domain.Entities.Mole import Mole
from Domain.Entities.NoneObject import NoneObject


class IObjFactory(metaclass=ABCMeta):
    @abstractmethod
    def get_obj(
        self, y: int, x: int, type: ObjectType, observer: IMoleObserver
    ) -> IRaiseObj:
        pass


class ObjFactory(IObjFactory):
    def get_obj(
        self, y: int, x: int, type: ObjectType, observer: IMoleObserver
    ) -> IRaiseObj:
        obj = None
        match type:
            case ObjectType.NONE:
                obj = NoneObject(observer)
            case ObjectType.BASIC_MOLE:
                obj = Mole(y, x, observer)
        return obj


class TestObjFactory(IObjFactory):
    def get_obj(
        self, y: int, x: int, type: ObjectType, observer: IMoleObserver
    ) -> IRaiseObj:
        obj = None
        match type:
            case ObjectType.NONE:
                obj = NoneObject()
            case ObjectType.BASIC_MOLE:
                obj = Mole(y, x, observer, 0.1)
        return obj
