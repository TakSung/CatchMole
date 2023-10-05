from abc import *
from Common.ObjectType import ObjectType


class IMoleObserver(metaclass=ABCMeta):
    @abstractmethod
    def update_state(self, type: ObjectType):
        pass


class IMoleSubject(metaclass=ABCMeta):
    @abstractmethod
    def notify_state(self):
        pass

    @abstractmethod
    def register_observer(self, observer: IMoleObserver):
        pass
