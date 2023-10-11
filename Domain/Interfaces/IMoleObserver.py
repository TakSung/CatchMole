from abc import *
from Common.ObjectType import ObjectType


class IMoleObserver(metaclass=ABCMeta):
    @abstractmethod
    def update_state(self, type: ObjectType) -> None:
        pass


class IMoleSubject(metaclass=ABCMeta):
    @abstractmethod
    def notify_state(self) -> None:
        pass

    @abstractmethod
    def register_observer(self, observer: IMoleObserver) -> None:
        pass
