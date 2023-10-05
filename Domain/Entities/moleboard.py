import random
import __init__
from Domain.Interfaces.IBoard import IBoard
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Interfaces.IMoleObserver import IMoleObserver
from Common.ObjectType import ObjectType

from Domain.Entities.ObjFactory import *


class MoleBoard(IBoard, IMoleObserver):
    size = (3, 3)

    def empty_map() -> list:
        return [[ObjectType.NONE]*MoleBoard.size[1] for _ in range(MoleBoard.size[0])]

    def __init__(self, factory: IObjFactory = ObjFactory()):
        self.board = MoleBoard.empty_map()
        self.factory = factory

    def get_state(self, y: int, x: int) -> ObjectType:
        return self.board[y][x]

    def raise_obj(self, y: int, x: int, type: ObjectType) -> IRaiseObj:
        obj = self.factory.get_obj(y, x, type, self)
        return obj

    def update_state(self, y: int, x: int, type: ObjectType) -> None:
        self.board[y][x] = type

    def print(self, tab: int = 2):
        for _ in range(tab):
            print("\t", end="")
        print("="*(2*self.size[1] + 1))

        for i in range(self.size[0]):
            for _ in range(tab):
                print("\t", end="")
            print(end="|")
            for j in range(self.size[1]):
                match(self.get_state(i, j)):
                    case ObjectType.NONE:
                        print("X", end="|")
                    case _:
                        print("O", end="|")
            print()
        for _ in range(tab):
            print("\t", end="")
        print("="*(2*self.size[1] + 1))


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
