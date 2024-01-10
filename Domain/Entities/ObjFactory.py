from abc import *
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Interfaces.IMoleObserver import IMoleObserver
from Common.ObjectType import ObjectType

from Domain.Entities.RaiseObject import *


class IObjFactory(metaclass=ABCMeta):
    @abstractmethod
    def get_obj(self, type: ObjectType) -> IRaiseObj:
        pass


class ObjFactory(IObjFactory):
    def get_obj(self, type: ObjectType) -> IRaiseObj:
        obj = None
        match type:
            case ObjectType.none:
                obj = NoneObject()
            case ObjectType.HACKER:
                obj = Hacker()
            case ObjectType.BASIC_MOLE:
                obj = Mole()
            case ObjectType.BOMB:
                obj = Bomb()
            case ObjectType.GOLD_MOLE:
                obj = Gold_Mole()
            case _:
                obj = NoneObject()
                print(f"Not Exist {type} in ObjFactory")
        return obj


class TestObjFactory(IObjFactory):
    def __init__(self, time=0.1):
        self.time = time

    def get_obj(self, type: ObjectType) -> IRaiseObj:
        obj = None
        match type:
            case ObjectType.none:
                obj = NoneObject()
            case ObjectType.BASIC_MOLE:
                obj = Mole(self.time)
            case ObjectType.HACKER:
                obj = Hacker(self.time)
            case ObjectType.BOMB:
                obj = Bomb()
            case ObjectType.GOLD_MOLE:
                obj = Gold_Mole(self.time)
            case _:
                obj = NoneObject()
                print(f"Not Exist {type} in ObjFactory")
        return obj
