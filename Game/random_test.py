import __init__
from typing import List, Callable
from Domain.Interfaces.IBoard import IBoard
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Interfaces.IBoardObserver import IBoardObserver
from Common.ObjectType import ObjectType

from Domain.Entities.ObjFactory import *
from Domain.Entities.MoleBoard import MoleBoard

import random


class BoardPrinter(IBoardObserver):
    def update_board(self, type: List[List[ObjectType]]) -> None:
        rows = len(type)
        cols = len(type[0])
        a = [str(i) for i in range(cols)]

        print("  " + " ".join(a))
        print(" ", "=" * (2 * cols + 1), sep="")
        for i in range(rows):
            print(i, end="|")
            for j in range(cols):
                match (type[i][j]):
                    case ObjectType.NONE:
                        print("X", end="|")
                    case _:
                        print("O", end="|")
            print()
        print(" ", "=" * (2 * cols + 1), sep="")


mole_board = MoleBoard()
printer = BoardPrinter()
mole_board.register_observer(printer)
## 램덤한 위치에 두더지 올리기

while True:
    ## 램덤한 xrandom yrandom 구하기
    xr = random.randrange(0, 4)
    yr = random.randrange(0, 4)

    mole_board.raise_obj(yr, xr, type=ObjectType.BASIC_MOLE)

    ##사용자한테 좌표 xplayer yplayer 받기
    xp = int(input())
    yp = int(input())

    t = mole_board.try_attack(yp, xp)
    print(t)
