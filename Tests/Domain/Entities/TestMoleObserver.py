from typing import List, Tuple, Optional
from Common import ObjectState, ObjectType
from Domain.Interfaces import IRaiseObj, IMoleObserver


class TestMoleObserver(IMoleObserver):
    def update_mole(self, y: int, x: int, type: ObjectType) -> None:
        self.mole: Tuple[int, int, ObjectType] = (y, x, type)

    def alert_result(
        self, y: int, x: int, type: ObjectType, state: ObjectState
    ) -> None:
        self.result: Tuple[int, int, ObjectType, ObjectState] = (y, x, type, state)

    def get_result(self) -> Optional[Tuple[int, int, ObjectType, ObjectState]]:
        try:
            return self.result
        except:
            return None

    def get_curent_mole(self) -> Optional[Tuple[int, int, ObjectType]]:
        try:
            return self.mole
        except:
            return None
