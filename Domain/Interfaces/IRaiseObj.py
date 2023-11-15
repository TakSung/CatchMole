from abc import *
from Common.ObjectType import *


class IRaiseObj(metaclass=ABCMeta):
    ## 올라가 있을때 때리면 때린 객체의 종류를 받고, 내려가 있느면 아무것도 안해고 NONE 을 반환한다.
    
    @abstractmethod
    ## 일어나 있을 때 자신의 상태를 알려준다.
    def get_state(self) -> ObjectType:
        pass

    @abstractmethod
    ## 올라가 있을 때 내려가게 하고, 내려가 있으면 그냥 내비둔다.
    def try_lower(self) -> None:
        pass

    @abstractmethod
    ## 올라가 있을때 때리면 때린 객체의 종류를 받고, 내려가 있느면 아무것도 안해고 NONE 을 반환한다.
    def try_attack(self) -> ObjectType:
        pass
    
