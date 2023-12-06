from abc import *
from collections.abc import Collection
from Common.PlayerState import PlayerState


class IPlayerStateObserver(metaclass=ABCMeta):
    @abstractmethod
    def update_state(self, state:PlayerState) -> None:
        pass


class IPlayerStateSubject(metaclass=ABCMeta):
    @abstractmethod
    def notify_player_state(self) -> None:
        pass

    @abstractmethod
    def register_player_state_observers(self, observers: Collection[IPlayerStateObserver]) -> None:
        pass