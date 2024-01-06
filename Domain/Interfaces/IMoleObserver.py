from abc import *
from collections.abc import Collection
from Common import ObjectType, ObjectState


class IMoleObserver(metaclass=ABCMeta):
    @abstractmethod
    def update_mole(self, y: int, x: int, type: ObjectType) -> None:
        pass

    @abstractmethod
    def alert_result(
        self, y: int, x: int, type: ObjectType, state: ObjectState
    ) -> None:
        pass


class IMoleSubject(metaclass=ABCMeta):
    @abstractmethod
    def notify_mole_state(self, state: ObjectState) -> None:
        pass

    @abstractmethod
    def register_mole_observers(self, observers: Collection[IMoleObserver]) -> None:
        pass
