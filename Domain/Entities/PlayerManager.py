import __init__
from typing import List, Union
from collections.abc import Collection


from Common import ObjectType, PlayerState, ObjectState
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Entities.RaiseObject import NoneObject
from Domain.Entities.ObjFactory import *
from Domain.Interfaces.IMoleObserver import IMoleSubject, IMoleObserver
from Domain.Interfaces.IPlayerStateObserver import (
    IPlayerStateSubject,
    IPlayerStateObserver,
)


class PlayerManager(IMoleObserver, IPlayerStateSubject):
    def __init__(
        self,
        state_observers: Union[
            Collection[IPlayerStateObserver], IPlayerStateObserver
        ] = [],
    ):
        match state_observers:
            case obsr if isinstance(obsr, IPlayerStateObserver):
                mole_observers = [obsr]
            case obsrs if isinstance(obsrs, Collection):
                pass
            case _:
                raise ValueError()
        self.register_player_state_observers(state_observers)

    def alert_result(
        self, y: int, x: int, type: ObjectType, state: ObjectState
    ) -> None:
        pass

    def update_mole(self, y: int, x: int, type: ObjectType, state: ObjectState) -> None:
        pass

    def notify_player_state(self) -> None:
        if self.state_observers == None:
            return
        for obsv in self.state_observers:
            match self.get_state():
                case ObjectType.HACKER:
                    obsv.update_state(PlayerState.Reverse)

    def register_player_state_observers(
        self, observers: Collection[IPlayerStateObserver]
    ) -> None:
        if observers is None:
            raise ValueError("RaiseHole in register_observers")
        for obsr in observers:
            self.state_observers.append(obsr)
