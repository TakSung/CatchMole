from abc import ABCMeta
import __init__
from icecream import ic

from typing import List
from collections.abc import Collection
from Domain.Interfaces.IBoard import IBoard
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Interfaces.IMoleObserver import IMoleObserver
from Domain.Interfaces.IBoardObserver import IBoardObserver, IBoardSubject
from Common.ObjectType import ObjectType

from Domain.Entities.ObjFactory import *
from Domain.Entities.RaiseHole import RaiseHole


class MoleBoard(IBoard, IMoleObserver, IBoardSubject):
    size = (4, 4)

    def empty_board(mole_observers:Collection[IMoleObserver], factory:IObjFactory) -> List[List[RaiseHole]]:
        return [[RaiseHole(y,x, mole_observers, factory) for x in range(MoleBoard.size[1])] for y in range(MoleBoard.size[0])]

    def empty_board_state() -> List[List[ObjectType]]:
        return [[ObjectType.NONE] * MoleBoard.size[1] for _ in range(MoleBoard.size[0])]

    def __init__(self,observers:List[IBoardObserver]=[], factory: IObjFactory = ObjFactory()):
        self.observers: List[IBoardObserver] = []
        match observers:
            case obsr if isinstance(obsr, IMoleObserver):
                observers = [obsr]
            case obsrs if isinstance(obsrs, Collection):
                pass
            case _:
                raise ValueError()

        self.register_board_observers(observers)
        self.register_board_observers(observers)
        self.board = MoleBoard.empty_board([self], factory)
        self.notify_board()

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
        self.notify_board()
        return ret 

    def set_obj(self, y: int, x: int, obj: IRaiseObj) -> IRaiseObj:
        ret = self.board[y][x].set_raise_object_to_raise_obj(obj)
        self.notify_board()
        return ret

    def try_attack(self, y: int, x: int) -> ObjectType:
        return self.board[y][x].try_attack()

    def update_state(self, y: int, x: int, type: ObjectType) -> None:
        self.notify_board()

    def register_mole_observers(self, observers: Collection[IMoleObserver])->None:
        if self.board is None:
            raise ValueError("MoleBoard NotExistBoard")
        
        for line in self.board:
            for raise_hole in line:
                raise_hole.register_mole_observers(observers)

    def register_board_observers(self, observers: Collection[IBoardObserver]) -> None:
        if observers is None:
            raise ValueError("MoleBoard in register_observers")
        for obsr in observers:
            self.observers.append(obsr)

    def notify_board(self) -> None:
        if self.observers is None:
            return
        for obsv in self.observers:
            obsv.update_board(self.get_board_state())

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
                    case ObjectType.NONE:
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
