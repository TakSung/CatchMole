import __init__
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Interfaces.IMoleObserver import IMoleSubject, IMoleObserver
from Common.ObjectType import ObjectType
import threading
import time


class Mole(IRaiseObj, IMoleSubject):

    # 두더지가 생성된 시점부터 일어나 있음 -> state
    def __init__(self, y: int, x: int, observer: IMoleObserver, timer: int = 2):
        self.state = True  # raise
        self.type = ObjectType.BASIC_MOLE
        self.x = x
        self.y = y
        self.register_observer(observer)
        self.lock = threading.Lock()

        def auto_lower():
            time.sleep(timer)
            self.try_lower()
        threading.Thread(target=auto_lower).start()
        self.notify_state()

    def try_lower(self) -> None:
        if not self.state:
            return

        self.lock.acquire()
        if self.state:
            self.state = False
        self.lock.release()

        self.notify_state()

    def try_attack(self) -> ObjectType:
        result = ObjectType.NONE

        self.lock.acquire()
        if self.state:
            result = self.type
            self.state = False
        self.lock.release()
        self.notify_state()

        return result

    def notify_state(self) -> None:
        if self.observer == None:
            return
        if self.state:
            self.observer.update_state(self.y, self.x, self.type)
        else:
            self.observer.update_state(self.y, self.x, ObjectType.NONE)

    def register_observer(self, observer: IMoleObserver) -> None:
        self.observer = observer
