from abc import *
from Common.ObjectType import *

    
class IPlayerAction(metaclass=ABCMeta):
    def action(self)-> None:
        pass
