from abc import ABCMeta
import __init__
from icecream import ic

from typing import List, Union, Tuple
from collections.abc import Collection
from Domain.Interfaces.IBoard import IBoard
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Interfaces.IMoleObserver import IMoleObserver, IMoleSubject
from Domain.Interfaces.IBoardObserver import IBoardObserver, IBoardSubject
from Common import ObjectType, ObjectState

from Domain.Entities.ObjFactory import *
from Domain.Entities.RaiseHole import RaiseHole


class MoleBoard(IBoard, IMoleObserver, IBoardSubject, IMoleSubject):
    def empty_board(
        size: Tuple[int, int],
        mole_observers: Collection[IMoleObserver],
        factory: IObjFactory,
    ) -> List[List[RaiseHole]]:
        """_summary_

        Args:
            size (Tuple[int,int]): y, x cordinate
            mole_observers (Collection[IMoleObserver]): _description_
            factory (IObjFactory): _description_

        Returns:
            List[List[RaiseHole]]: _description_
        """
        return [
            [RaiseHole(y, x, mole_observers, factory) for x in range(size[1])]
            for y in range(size[0])
        ]

    def empty_board_state(size: Tuple[int, int]) -> List[List[ObjectType]]:
        """_summary_

        Args:
            size (Tuple[int,int]): y,x cordinate

        Returns:
            List[List[ObjectType]]: _description_
        """
        return [[ObjectType.none] * size[1] for _ in range(size[0])]

    def __init__(
        self,
        size: Tuple[int, int] = (4, 4),
        board_observers: Union[List[IBoardObserver], IBoardObserver] = [],
        mole_observers: Union[List[IMoleObserver], IMoleObserver] = [],
        factory: IObjFactory = ObjFactory(),
    ):
        self.size = size
        self.board_observers: List[IBoardObserver] = []
        match board_observers:
            case obsr if isinstance(obsr, IBoardObserver):
                observers = [obsr]
            case obsrs if isinstance(obsrs, Collection):
                observers = obsrs
            case _:
                raise ValueError()

        self.register_board_observers(observers)
        self.board: List[List[RaiseHole]] = MoleBoard.empty_board(
            self.get_size(), [self], factory
        )
        self.notify_board()

        match mole_observers:
            case obsr if isinstance(obsr, IMoleObserver):
                observers = [obsr]
            case obsrs if isinstance(obsrs, Collection):
                observers = obsrs
            case _:
                raise ValueError()
        self.register_mole_observers(observers)

    def get_board_state(self) -> List[List[ObjectType]]:
        ret = []
        for y in range(self.size[0]):
            ret1 = []
            for x in range(self.size[1]):
                ret1.append(self.board[y][x].get_state())
            ret.append(ret1)
        return ret

    def get_state(self, y: int, x: int) -> ObjectType:
        return self.board[y][x].get_state()

    def raise_obj(self, y: int, x: int, type: ObjectType) -> IRaiseObj:
        ret = self.board[y][x].set_raise_object_to_type(type)
        # self.notify_board()
        return ret

    def set_obj(self, y: int, x: int, obj: IRaiseObj) -> IRaiseObj:
        ret = self.board[y][x].set_raise_object_to_raise_obj(obj)
        # self.notify_board()
        return ret

    def try_attack(self, y: int, x: int) -> ObjectType:
        return self.board[y][x].try_attack()

    def alert_result(
        self, y: int, x: int, type: ObjectType, state: ObjectState
    ) -> None:
        pass

    def update_mole(self, y: int, x: int, type: ObjectType) -> None:
        self.notify_board()

    def notify_mole_state(self, state: ObjectState) -> None:
        pass

    def register_mole_observers(self, observers: Collection[IMoleObserver]) -> None:
        if observers is None:
            raise ValueError("MoleBoard in register_observers")
        for line in self.board:
            for obj in line:
                obj.register_mole_observers(observers)

    def register_board_observers(self, observers: Collection[IBoardObserver]) -> None:
        if observers is None:
            raise ValueError("MoleBoard in register_observers")
        for obsr in observers:
            self.board_observers.append(obsr)

    def notify_board(self) -> None:
        if self.board_observers is None:
            return
        for obsv in self.board_observers:
            obsv.update_board(self.get_board_state())

    def get_size(self) -> Tuple[int, int]:
        return self.size

    def print(self, tab: int = 2):
        for _ in range(tab):
            print("\t", end="")
        print("=" * (2 * self.size[1] + 1))

        for i in range(self.size[0]):
            for _ in range(tab):
                print("\t", end="")
            print(end="|")
            for j in range(self.size[1]):
                match (self.get_state(i, j)):
                    case ObjectType.none:
                        print("X", end="|")
                    case _:
                        print("O", end="|")
            print()
        for _ in range(tab):
            print("\t", end="")
        print("=" * (2 * self.size[1] + 1))


# a = random.randrange(0, 3)
# b = random.randrange(0, 3)

# Board = [[0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0]]

# Board[a][b] = 1

# for x, y, z in Board:
#     print(x, y, z)

# class moleboard(IBoard)

# if __name__ == '__main__':
# 1 print board
# 2 raise mole and print board
# 3 random raise mole and print board
