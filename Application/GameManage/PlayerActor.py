import __init__
from collections.abc import Collection
from typing import Tuple, List

from Common import PlayerState, ObjectType, ObjectState
from Domain.Interfaces import IPlayerStateObserver, IBoard, IMoleObserver, IMoleSubject
from Domain.Entities.Cursor import Cursor
from Application.KeyAction import (
    PlayerDownArrowAction,
    PlayerLeftArrowAction,
    PlayerRightArrowAction,
    PlayerUpArrowAction,
)


class PlayerCursorControl(IPlayerStateObserver):
    def __init__(self, size: int):
        self.cursor = Cursor(size)
        self.right_action = PlayerRightArrowAction(self.cursor)
        self.left_action = PlayerLeftArrowAction(self.cursor)
        self.up_action = PlayerUpArrowAction(self.cursor)
        self.down_action = PlayerDownArrowAction(self.cursor)
        self.state = PlayerState.Nomal

    def get_cursor(self) -> Tuple[int, int]:
        """_summary_
        tuple형태로 y,x를 반환한다.

        Returns:
            Tuple[int,int]: return (y,x)
        """
        return self.cursor.get()

    def get_state(self) -> PlayerState:
        return self.state

    def set_state(self, state: PlayerState):
        self.state = state

    def right(self):
        self.right_action.action()

    def left(self):
        self.left_action.action()

    def up(self):
        self.up_action.action()

    def down(self):
        self.down_action.action()

    def update_state(self, state: PlayerState) -> None:
        self.set_state(state)

        self.right_action.update_state(state)
        self.left_action.update_state(state)
        self.up_action.update_state(state)
        self.down_action.update_state(state)


class PlayerActor(PlayerCursorControl, IMoleSubject):
    def __init__(
        self,
        id: int,
        board: IBoard,
        catch_observers: Collection[IMoleObserver] = [],
    ):
        super().__init__(board.get_size())
        self.id = id
        self.board = board
        self.recode: List[Tuple[int, int, ObjectType]] = []
        self.mole_observers: List[IMoleObserver] = []
        self.register_mole_observers(catch_observers)

    def try_attack(self) -> ObjectType:
        (y, x) = self.cursor.get()
        type = self.board.try_attack(y, x)
        if type is not ObjectType.none:
            self.update_catch_obj(y, x, type)
        return type

    def update_catch_obj(self, y: int, x: int, type: ObjectType):
        self.recode.append((y, x, type))
        self.notify_mole_state(ObjectState.CATCHED)

    def notify_mole_state(self, state: ObjectState) -> None:
        (y, x, type) = self.recode[-1]
        if self.mole_observers == None:
            return
        for obsv in self.mole_observers:
            obsv.update_mole(y, x, type)
            obsv.alert_result(y, x, type, state)

    def register_mole_observers(self, observers: Collection[IMoleObserver]) -> None:
        match observers:
            case observers if isinstance(observers, Collection):
                for obsr in observers:
                    self.mole_observers.append(obsr)
            case _:
                raise ValueError("RaiseHole in register_observers")
