import __init__
from typing import List, Union
from collections.abc import Collection


from Common import ObjectType, ObjectState
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Entities.RaiseObject import NoneObject
from Domain.Entities.ObjFactory import *
from Domain.Interfaces.IMoleObserver import IMoleSubject, IMoleObserver

# from icecream import ic


class RaiseHole(IRaiseObj, IMoleSubject):
    none_obj = NoneObject()

    def __init__(
        self,
        y: int,
        x: int,
        mole_observers: Union[Collection[IMoleObserver], IMoleObserver] = [],
        factory: IObjFactory = ObjFactory(),
    ):
        self.y = y
        self.x = x
        self.raise_obj = None
        self.set_none_object()
        self.mole_observers: List[IMoleObserver] = []
        self.before_type = ObjectType.none
        self.factory = factory
        match mole_observers:
            case obsr if isinstance(obsr, IMoleObserver):
                mole_observers = [obsr]
            case obsrs if isinstance(obsrs, Collection):
                pass
            case _:
                raise ValueError()
        self.register_mole_observers(mole_observers)

    def set_none_object(self) -> IRaiseObj:
        if not isinstance(self.raise_obj, NoneObject):
            self.raise_obj = self.none_obj
        return self.raise_obj

    def set_timer(self, time: float) -> None:
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

    def set_raise_object_to_type(self, object_type: ObjectType) -> IRaiseObj:
        """
        raise_obj가 NoneObject이면 object_type으로 객체 생성
        """
        if self.get_state() == ObjectType.none:
            self.raise_obj = self.factory.get_obj(object_type)
            self.notify_mole_state(ObjectState.RAISE_OBJECT)
            self.before_type = self.get_state()
            self.run_timer()
        return self.raise_obj

    def set_raise_object_to_raise_obj(self, obj: IRaiseObj) -> IRaiseObj:
        if self.get_state() == ObjectType.none:
            self.raise_obj = obj
            self.run_timer()
        return self.raise_obj

    def notify_mole_state(self, state: ObjectState) -> None:
        if self.mole_observers == None:
            return
        for obsv in self.mole_observers:
            obsv.update_mole(self.y, self.x, self.get_state())
            obsv.alert_result(self.y, self.x, self.before_type, state)

    def register_mole_observers(self, observers: Collection[IMoleObserver]) -> None:
        match observers:
            case observers if isinstance(observers, Collection):
                for obsr in observers:
                    self.mole_observers.append(obsr)
            case _:
                raise ValueError("RaiseHole in register_observers")

    ## 일어나 있을 때 자신의 상태를 알려준다.
    def get_state(self) -> ObjectType:
        return self.raise_obj.get_state()

    ## 올라가 있을 때 내려가게 하고, 내려가 있으면 그냥 내비둔다.
    def try_lower(self) -> None:
        before_type = self.get_state()
        self.raise_obj.try_lower()
        if self.get_state() == ObjectType.none and not isinstance(
            self.raise_obj, NoneObject
        ):
            self.set_none_object()
            self.before_type = before_type
            self.notify_mole_state(ObjectState.LOW)

    ## 올라가 있을때 때리면 때린 객체의 종류를 받고, 내려가 있느면 아무것도 안해고 NONE 을 반환한다.
    def try_attack(self) -> ObjectType:
        before_type = self.get_state()
        result = self.raise_obj.try_attack()

        if self.get_state() == ObjectType.none and not isinstance(
            self.raise_obj, NoneObject
        ):
            self.set_none_object()
            self.before_type = before_type
            self.notify_mole_state(ObjectState.CATCHED)

        return result
