import __init__

from collections.abc import Collection
from typing import Tuple, Union, List

from Common import PlayerState, ObjectType, ObjectState
from Domain.Interfaces import IBoard
from Application.StateFilter import (
    ObjectPlayerLinker,
    BuffFilter,
    DebuffFilter,
    IConvertObjectToState,
)

from Application.GameManage import PlayerActor


class OneBoardGameManager:
    def __init__(
        self,
        board: IBoard,
        player_num: int = 2,
        buff_filter: IConvertObjectToState = BuffFilter(),
        debuff_filter: IConvertObjectToState = DebuffFilter(3),
    ) -> None:
        self.player_list: List[PlayerActor] = [
            PlayerActor(i, board) for i in range(player_num)
        ]
        self.debuff_linker_list: List[ObjectPlayerLinker] = []
        for id in range(player_num):
            players = [self.player_list[i] for i in range(player_num) if i != id]
            self.debuff_linker_list.append(
                ObjectPlayerLinker(
                    players,
                    self.player_list[id],
                    debuff_filter,
                )
            )
        self.buff_linker_list: List[ObjectPlayerLinker] = []
        for player in self.player_list:
            self.buff_linker_list.append(
                ObjectPlayerLinker(
                    [player],
                    player,
                    buff_filter,
                )
            )
