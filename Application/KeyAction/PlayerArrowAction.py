import __init__
from typing import Dict

from Domain.Entities.Cursor import Cursor
from Domain.Interfaces import IPlayerAction
from Application.PlayerAcion import *

class PlayerRightArrowAction(IPlayerAction):
    def __init(self, cursor:Cursor):
        self.cursor = cursor
        self.state = PlayerState.Nomal
        self.state_action_dict:Dict[PlayerState, IPlayerAction]= {
            PlayerState.Nomal : CursorRightAction(cursor),
            PlayerState.Reverse : CursorLeftAction(cursor)
        }

    def action(self) -> None:
        self.state_action_dict[self.state]
    
class PlayerLeftArrowAction(IPlayerAction):
    def __init(self, cursor:Cursor):
        self.cursor = cursor
        self.state = PlayerState.Nomal
        self.state_action_dict:Dict[PlayerState, IPlayerAction]= {
            PlayerState.Nomal : 
            PlayerState.Reverse :
        }

    def action(self) -> None:
        self.state_action_dict[self.state]
    
class PlayerUpArrowAction(IPlayerAction):
    def __init(self, cursor:Cursor):
        self.cursor = cursor
        self.state = PlayerState.Nomal
        self.state_action_dict:Dict[PlayerState, IPlayerAction]= {
            PlayerState.Nomal : 
            PlayerState.Reverse :
        }

    def action(self) -> None:
        self.state_action_dict[self.state]
    
class PlayerDownArrowAction(IPlayerAction):
    def __init(self, cursor:Cursor):
        self.cursor = cursor
        self.state = PlayerState.Nomal
        self.state_action_dict:Dict[PlayerState, IPlayerAction]= {
            PlayerState.Nomal : 
            PlayerState.Reverse : 
        }

    def action(self) -> None:
        self.state_action_dict[self.state]
    