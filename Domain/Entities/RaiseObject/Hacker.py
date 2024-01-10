import __init__
from typing import Union
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Common.ObjectType import ObjectType
import threading


class Hacker(IRaiseObj):
    # 두더지가 생성된 시점부터 일어나 있음 -> state
    # 두더지가 특정 시간이 지나면 저절로 아래로 내려감
    def __init__(self, timer: Union[int, float] = 10):
        # 두더지가 특정 시간이 지나면 저절로 아래로 내려감
        self.state = True  # raise
        self.type = ObjectType.HACKER
        self.lock = threading.Lock()
        self.set_timer(timer)

    def try_lower(self) -> None:
        if not self.state:
            return

        self.lock.acquire()
        if self.state:
            self.state = False
        self.lock.release()

    def try_attack(self) -> ObjectType:
        result = ObjectType.none

        self.lock.acquire()
        if self.state:
            result = self.type
            self.state = False
        self.lock.release()

        return result

    def get_state(self) -> ObjectType:
        if self.state:
            return self.type
        else:
            return ObjectType.none
