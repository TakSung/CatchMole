import __init__
from typing import List
from Domain.Interfaces.IBoard import IBoard
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Interfaces.IMoleObserver import IMoleObserver
from Common.ObjectType import ObjectType

from Domain.Entities.ObjFactory import *
from Domain.Entities.NoneObject import NoneObject


class MoleBoard(IBoard, IMoleObserver):
    size = (3, 3)

    def empty_board() -> List[List[IRaiseObj]]:
        return [[NoneObject()]*MoleBoard.size[1] for _ in range(MoleBoard.size[0])]

    def empty_board_state() -> List[List[ObjectType]]:
        return [[ObjectType.NONE]*MoleBoard.size[1] for _ in range(MoleBoard.size[0])]

    def __init__(self, factory: IObjFactory = ObjFactory()):
        self.board = MoleBoard.empty_board()
        self.factory = factory

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
        obj = self.factory.get_obj(type, self)
        self.board[y][x] = obj
        return obj

    def set_obj(self, y: int, x: int, obj: IRaiseObj) -> IRaiseObj:
        obj.register_observer(self)
        self.board[y][x] = obj
        return obj

    def try_attack(self, y: int, x: int) -> ObjectType:
        return self.board[y][x].try_attack()

    def update_state(self, type: ObjectType) -> None:
        print("plz implement MoleBoard.update_state.")

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
