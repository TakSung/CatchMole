import __init__
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Interfaces.IMoleObserver import IMoleSubject, IMoleObserver
from Common.ObjectType import ObjectType


class NoneObject(IRaiseObj):
    def __init__(self):
        self.type = ObjectType.NONE

    def try_lower(self) -> None:
        pass

    def try_attack(self) -> ObjectType:
        return self.get_state()

    def get_state(self) -> ObjectType:
        return self.type

    # def notify_state(self) -> None:
    #     if self.observer == None:
    #         return
    #     self.observer.update_state(self.get_state())

    # def register_observer(self, observer: IMoleObserver) -> None:
    #     self.observer = observer
