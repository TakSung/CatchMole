from abc import *
from typing import List,Union
from collections.abc import Collection
from Common.ObjectType import ObjectType


class IBoardObserver(metaclass=ABCMeta):
    @abstractmethod
    def update_board(self, board: List[List[ObjectType]]) -> None:
        pass


class IBoardSubject(metaclass=ABCMeta):
    @abstractmethod
    def notify_board(self) -> None:
        pass

    @abstractmethod
    def register_board_observers(self, observers: Collection[IBoardObserver]) -> None:
        pass
