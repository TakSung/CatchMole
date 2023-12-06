import __init__

from typing import Tuple

from Common import PlayerState
from Domain.Interfaces import IPlayerStateObserver
from Domain.Entities.Cursor import Cursor
from Application.KeyAction import PlayerDownArrowAction,PlayerLeftArrowAction,PlayerRightArrowAction, PlayerUpArrowAction

class PlayerActionSet(IPlayerStateObserver):

    def __init__(self, size:int):
        self.cursor = Cursor(size)
        self.right_action = PlayerRightArrowAction(self.cursor)
        self.left_action = PlayerLeftArrowAction(self.cursor)
        self.up_action = PlayerUpArrowAction(self.cursor)
        self.down_action = PlayerDownArrowAction(self.cursor)
        self.state = PlayerState.Nomal
        
    def get_cursor(self)->Tuple[int,int]:
        """_summary_
        tuple형태로 y,x를 반환한다.

        Returns:
            Tuple[int,int]: return (y,x)
        """
        return self.cursor.get()
    
    def get_state(self)->PlayerState:
        return self.state
    def set_state(self, state:PlayerState):
        self.state = state
    
    def right(self):
        self.right_action.action()
    def left(self):
        self.left_action.action()
    def up(self):
        self.up_action.action()
    def down(self):
        self.down_action.action()
        
    def update_state(self, state:PlayerState) -> None:
        self.set_state(state)
        
        self.right_action.update_state(state)
        self.left_action.update_state(state)
        self.up_action.update_state(state)
        self.down_action.update_state(state)