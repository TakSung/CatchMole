import __init__
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Interfaces.IMoleObserver import IMoleSubject, IMoleObserver
from Common.ObjectType import ObjectType
import threading


class mole(IRaiseObj, IMoleSubject):
    # 두더지가 생성된 시점부터 일어나 있음 -> state
    def __init__(self, y: int, x: int, observer: IMoleObserver):
        self.state = True  # raise
        self.type = ObjectType.BASIC_MOLE
        self.x = x
        self.y = y
        self.register_observer(observer)
        self.lock = threading.Lock()

    def try_lower(self) -> None:
        if not self.state:
            return

        self.lock.acquire()
        if self.state:
            self.state = False
        self.lock.release()

    def try_attack(self) -> ObjectType:
        result = ObjectType.NONE
        self.lock.acquire()

        if self.state:
            result = self.type
            self.state = False

        self.lock.release()
        return result

    def notify_state(self):
        self.observer.update_state(self.type)

    def register_observer(self, observer: IMoleObserver):
        self.observer = observer
