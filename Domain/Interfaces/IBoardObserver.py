from abc import *
from typing import List
from Common.ObjectType import ObjectType


class IBoardObserver(metaclass=ABCMeta):
    @abstractmethod
    def update_board(self, type: List[List[ObjectType]]) -> None:
        pass


class IBoardSubject(metaclass=ABCMeta):
    @abstractmethod
    def notify_board(self) -> None:
        pass

    @abstractmethod
    def register_observer(self, observer: IBoardObserver) -> None:
        pass
