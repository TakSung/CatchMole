from abc import *
from Common.ObjectType import *


class IRaiseObj(metaclass=ABCMeta):
    @abstractmethod
    def try_lower(self) -> None:
        pass

    @abstractmethod
    def try_attack(self) -> ObjectType:
        pass
