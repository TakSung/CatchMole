import __init__
from typing import List
from Domain.Interfaces.IBoard import IBoard
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Interfaces.IMoleObserver import IMoleObserver
from Common.ObjectType import ObjectType

from Domain.Entities.ObjFactory import *
from Domain.Entities.MoleBoard import MoleBoard

import random

mole_board = MoleBoard()
## 램덤한 위치에 두더지 올리기


while True:
    ## 램덤한 xrandom yrandom 구하기
    xr = random.randrange(0,4)
    yr = random.randrange(0,4)

    mole_board.raise_obj(yr, xr, type = ObjectType.BASIC_MOLE)
    

    ##사용자한테 좌표 xplayer yplayer 받기
    xp = int(input())
    yp = int(input())

    t = mole_board.try_attack(yp, xp)
    print(t)


