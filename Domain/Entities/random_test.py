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

## 램덤한 x y 구하기
xr = random.randrange(0,4)
yr = random.randrange(0,4)

mole_board.raise_obj(y = yr, x = xr, type = ObjectType.BASIC_MOLE)
mole_board.print()