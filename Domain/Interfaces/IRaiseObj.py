from abc import *
from Common.MoleType import *


class IRaiseObj(metaclass=ABCMeta):
    @abstractmethod
    def try_lower() -> None:
        pass

    @abstractmethod
    def try_attack() -> ObjectType:
        pass
