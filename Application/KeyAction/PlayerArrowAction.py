import __init__
from typing import Dict

from Common import PlayerState
from Domain.Entities.Cursor import Cursor
from Domain.Interfaces import IPlayerAction, IPlayerStateObserver
from Application.PlayerAcion import CursorDownAction,CursorLeftAction,CursorRightAction,CursorUpAction

class PlayerArrowAction(IPlayerAction, IPlayerStateObserver):
    def __init__(
        self, 
        nomal_action:IPlayerAction,
        reverse_action:IPlayerAction
        ):
        self.state = PlayerState.Nomal
        self.state_action_dict:Dict[PlayerState, IPlayerAction]= {
            PlayerState.Nomal : nomal_action,
            PlayerState.Reverse : reverse_action
        }

    def action(self) -> None:
        self.state_action_dict[self.state].action()
        
    def update_state(self, state:PlayerState) -> None:
        match state:
            case PlayerState.Nomal:
                self.state = PlayerState.Nomal
            case PlayerState.Reverse:
                self.state = PlayerState.Reverse

class PlayerRightArrowAction(PlayerArrowAction):
    def __init__(self, cursor:Cursor):
        super().__init__(CursorRightAction(cursor), CursorLeftAction(cursor))
        self.cursor = cursor

    
class PlayerLeftArrowAction(PlayerArrowAction):
    def __init__(self, cursor:Cursor):
        super().__init__(CursorLeftAction(cursor), CursorRightAction(cursor))
        self.cursor = cursor
    
class PlayerUpArrowAction(PlayerArrowAction):
    def __init__(self, cursor:Cursor):
        super().__init__(CursorUpAction(cursor), CursorDownAction(cursor))
        self.cursor = cursor
    
class PlayerDownArrowAction(PlayerArrowAction):
    def __init__(self, cursor:Cursor):
        super().__init__(CursorDownAction(cursor), CursorUpAction(cursor))
        self.cursor = cursor