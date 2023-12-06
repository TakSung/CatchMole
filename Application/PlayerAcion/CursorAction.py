import __init__

from Common import PlayerState
from Domain.Entities.Cursor import Cursor
from Domain.Interfaces import IPlayerAction

class CursorRightAction(IPlayerAction):
    def __init__(self, cursor:Cursor):
        self.cursor = cursor

    def action(self) -> None:
        self.cursor.set(x=self.cursor.get_x()+1)
    
class CursorLeftAction(IPlayerAction):
    def __init__(self, cursor:Cursor):
        self.cursor = cursor

    def action(self) -> None:
        self.cursor.set(x=self.cursor.get_x()-1)
    
class CursorUpAction(IPlayerAction):
    def __init__(self, cursor:Cursor):
        self.cursor = cursor

    def action(self) -> None:
        self.cursor.set(y=self.cursor.get_y()+1)
    
class CursorDownAction(IPlayerAction):
    def __init__(self, cursor:Cursor):
        self.cursor = cursor

    def action(self) -> None:
        self.cursor.set(y=self.cursor.get_y()-1)
    