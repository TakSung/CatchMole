import sys
from pathlib import Path

now_path = Path(__file__).parent
root_path = str(now_path.parent.parent)

if not (root_path in sys.path):
    sys.path.append(root_path)

from Domain.Entities.RaiseHole import RaiseHole
from Domain.Entities.MoleBoard import MoleBoard
from Domain.Entities.ObjFactory import ObjFactory, IObjFactory, TestObjFactory
