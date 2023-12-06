import __init__

from collections.abc import Collection
from typing import Tuple,Union

from Common import PlayerState
from Domain.Interfaces import IPlayerStateObserver, IPlayerStateSubject, IMoleObserver,IMoleSubject
from Domain.Entities.Cursor import Cursor
from Application.KeyAction import PlayerDownArrowAction,PlayerLeftArrowAction,PlayerRightArrowAction, PlayerUpArrowAction
from Application.GameManage import PlayerActionSet

class PlayerManager(IPlayerStateSubject, IMoleObserver):
    def __init__(
        self,
        debuff_matchs:Union[Collection[Tuple[IPlayerStateObserver, IMoleSubject]], None]=None,
        buff_matchs:Union[Collection[Tuple[IPlayerStateObserver, IMoleSubject]], None])=None:
        
