import __init__

from collections.abc import Collection
from typing import List

from Common import PlayerState, ObjectType, ObjectState
from Domain.Interfaces import (
    IPlayerStateObserver,
    IPlayerStateSubject,
    IMoleObserver,
    IMoleSubject,
)

from Application.StateFilter import IConvertObjectToState


class ObjectPlayerLinker(IPlayerStateSubject, IMoleObserver):
    """_summary_
    플레이어 상태와 두더지 잡은 상태를 연결시켜준다

    Args:
        IPlayerStateSubject (_type_): _description_
        IMoleObserver (_type_): _description_
    """

    def __init__(
        self,
        players: Collection[IPlayerStateObserver],
        mole: IMoleSubject,
        converter: IConvertObjectToState,
    ):
        """_summary_
        두더지 구멍과 플레이어를 이어준다. 잡힌 두더지가 플레이어에게 어떤 영향을 주는지 기술한 state_func 함수를 인자로 넣어준다.

        Args:
            players (Collection[IPlayerStateObserver]): _description_
            mole (IMoleSubject): _description_
            state_func (Callable[[int,int,ObjectType], Tuple[PlayerState,float]]): _description_ paramater(y,x,type), return(state, timer) 타이머가 0이면 실행하지 않는다.
        """
        self.players: List[IPlayerStateObserver] = []
        self.register_player_state_observers(players)
        mole.register_mole_observers([self])
        self.converter = converter

    def notify_player_state(self) -> None:
        """_summary_
        실행하면 정상상태로 돌린다.
        """
        state = PlayerState.Nomal
        for p in self.players:
            p.update_state(state)

    def register_player_state_observers(
        self, observers: Collection[IPlayerStateObserver]
    ) -> None:
        for obsr in observers:
            self.players.append(obsr)

    def alert_result(
        self, y: int, x: int, type: ObjectType, state: ObjectState
    ) -> None:
        """_summary_
        mole이 전파한 정보를 업데이트 한다.
        인자로 받은 함수를 사용하여 스트레티지 하게 상태를 전파한다.
        일정시간이 지난 이후 노멀상태로 돌아가게 한다.
        Args:
            y (int): _description_:
            x (int): _description_
            type (ObjectType): _description_
        """
        match state:
            case ObjectState.CATCHED:
                (state, time) = self.converter.convert(y, x, type)
                for p in self.players:
                    p.update_state(state)

                self.run_timer(time)
            case _:
                print(f"not defined '{state}' in ObjectPlayerLinker.alert_result")

    def update_mole(self, y: int, x: int, type: ObjectType) -> None:
        """_summary_
        mole이 전파한 정보를 업데이트 한다.
        인자로 받은 함수를 사용하여 스트레티지 하게 상태를 전파한다.
        일정시간이 지난 이후 노멀상태로 돌아가게 한다.
        Args:
            y (int): _description_:
            x (int): _description_
            type (ObjectType): _description_
        """
        pass

    def run_timer(self, time: float):
        """_summary_
        일정 시간 이후 notify_player_state() 를 실행 시킨다.

        Args:
            time (float): _description_ 타이머가 0이면 실행하지 않는다.
        """
        if time <= 0:
            return

        import threading
        import time as timer

        def auto_nomal():
            timer.sleep(time)
            self.notify_player_state()

        threading.Thread(target=auto_nomal).start()
