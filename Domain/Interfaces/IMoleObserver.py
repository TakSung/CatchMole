from abc import *
from Common.MoleType import MoleType


class IMoleObserver(metaclass=ABCMeta):
    @abstractmethod
    def update_state(type: MoleType):
        pass


class IMoleSubject(metaclass=ABCMeta):
    @abstractmethod
    def notify_state():
        pass

    @abstractmethod
    def register_observer(observer: IMoleObserver):
        pass
