import __init__
from typing import Union
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Interfaces.IMoleObserver import IMoleSubject, IMoleObserver
from Common.ObjectType import ObjectType
import threading

class Mole(IRaiseObj):
    # 두더지가 생성된 시점부터 일어나 있음 -> state
<<<<<<<< HEAD:Domain/Entities/mole.py
<<<<<<<<< Temporary merge branch 1
    # 두더지가 특정 시간이 지나면 저절로 아래로 내려감
    def __init__(self, observer: IMoleObserver, timer: int = 2):
=========
    def __init__(self, observer: IMoleObserver, timer: int = 10):
>>>>>>>>> Temporary merge branch 2
========
    def __init__(self, timer: Union[int,float] = 10):
        # 두더지가 특정 시간이 지나면 저절로 아래로 내려감

>>>>>>>> 7d08a72e43e51ca501ea48af77476487c9e85c0c:Domain/Entities/RaiseObject/Mole.py
        self.state = True  # raise
        self.type = ObjectType.BASIC_MOLE
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
        result = ObjectType.NONE

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
            return ObjectType.NONE

    