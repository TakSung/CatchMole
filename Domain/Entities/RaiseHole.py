import __init__
from typing import List, Union
from collections.abc import Collection


from Common.ObjectType import ObjectType
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Entities.RaiseObject import NoneObject
from Domain.Entities.ObjFactory import *
from Domain.Interfaces.IMoleObserver import IMoleSubject, IMoleObserver
from Common.ObjectType import ObjectType

class RaiseHole(IRaiseObj, IMoleSubject):
    
    def __init__(self, y: int, x: int, observers: Union[Collection[IMoleObserver], IMoleObserver]=[], factory:IObjFactory = ObjFactory()):
        self.y = y
        self.x = x
        self.raise_obj = NoneObject()
        self.observers:List[IMoleObserver] = []
        self.factory = factory
        match observers:
            case obsr if isinstance(obsr, IMoleObserver):
                observers = [obsr]
            case obsrs if isinstance(obsrs, Collection):
                pass
            case _:
                raise ValueError()
        self.register_observers(observers)
    
    def set_none_object(self)->IRaiseObj:
        if not isinstance(self.raise_obj, NoneObject):
            self.raise_obj = NoneObject()
        return self.raise_obj
    
    def set_timer(self, time:float) -> None:
        self.raise_obj.set_timer(time)
        
    def get_time(self) -> float:
        return self.raise_obj.get_time()
    
    def run_timer(self):
        import threading
        import time
        
        def auto_lower():
            time.sleep(self.get_time())
            self.try_lower()

        threading.Thread(target=auto_lower).start()

    def set_raise_object_to_type(self, object_type:ObjectType)->IRaiseObj:
        '''
        raise_obj가 NoneObject이면 object_type으로 객체 생성
        '''
        if self.raise_obj.get_state() == ObjectType.NONE:
            self.raise_obj = self.factory.get_obj(object_type)
        self.run_timer()
        return self.raise_obj
    
    def set_raise_object_to_raise_obj(self, obj:IRaiseObj)->IRaiseObj:
        self.raise_obj = obj
        self.run_timer()
        return self.raise_obj
        
    def notify_state(self) -> None:
        if self.observers == None:
            return
        for obsv in self.observers:
            obsv.update_state(self.y, self.x, self.get_state())

    def register_observers(self, observers: Collection[IMoleObserver]) -> None:
        if observers is None:
            raise ValueError("RaiseHole in register_observers")
        for obsr in observers:
            self.observers.append(obsr)

    ## 일어나 있을 때 자신의 상태를 알려준다.
    def get_state(self) -> ObjectType:
        return self.raise_obj.get_state()

    
    ## 올라가 있을 때 내려가게 하고, 내려가 있으면 그냥 내비둔다.
    def try_lower(self) -> None:
        self.raise_obj.try_lower()
        if self.raise_obj.get_state() == ObjectType.NONE and not isinstance(self.raise_obj, NoneObject):
            self.set_none_object()
            self.notify_state()

    
    ## 올라가 있을때 때리면 때린 객체의 종류를 받고, 내려가 있느면 아무것도 안해고 NONE 을 반환한다.
    def try_attack(self) -> ObjectType:
        result = self.raise_obj.try_attack()

        if self.raise_obj.get_state() == ObjectType.NONE and not isinstance(self.raise_obj, NoneObject):
            self.set_none_object()
            self.notify_state()
        
        return result
    
    
    