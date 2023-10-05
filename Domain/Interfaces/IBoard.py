from abc import *
from Common.MoleType import *


class IBoard(metaclass=ABCMeta):
    @abstractmethod
    def get_state(y: int, x: int) -> MoleType:
        pass

    @abstractmethod
    def raise_mole(y: int, x: int, type: MoleType) -> None:
        pass
