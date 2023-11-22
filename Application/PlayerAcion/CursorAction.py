import __init__

from Domain.Entities.Cursor import Cursor
from Domain.Interfaces import IPlayerAction

class CursorRightAction(IPlayerAction):
    def __init(self, cursor:Cursor):
        self.cursor = cursor

    def action(self) -> None:
        raise NotImplementedError()
    
class CursorLeftAction(IPlayerAction):
    def __init(self, cursor:Cursor):
        self.cursor = cursor

    def action(self) -> None:
        raise NotImplementedError()
    
class CursorUPAction(IPlayerAction):
    def __init(self, cursor:Cursor):
        self.cursor = cursor

    def action(self) -> None:
        raise NotImplementedError()
    
class CursorDownAction(IPlayerAction):
    def __init(self, cursor:Cursor):
        self.cursor = cursor

    def action(self) -> None:
        raise NotImplementedError()
    