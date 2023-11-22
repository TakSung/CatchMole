import sys
from pathlib import Path

now_path = Path(__file__).parent
root_path = str(now_path.parent.parent)

if not (root_path in sys.path):
    sys.path.append(root_path)

from Domain.Interfaces.IBoard import IBoard
from Domain.Interfaces.IBoardObserver import IBoardObserver, IBoardSubject
from Domain.Interfaces.IMoleObserver import IMoleObserver, IMoleSubject
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Interfaces.IPlayerAction import IPlayerAction
