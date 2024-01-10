import sys
from pathlib import Path

now_path = Path(__file__).parent
root_path = str(now_path.parent.parent.parent)

if not (root_path in sys.path):
    sys.path.append(root_path)

from Domain.Entities.RaiseObject.Mole import Mole
from Domain.Entities.RaiseObject.NoneObject import NoneObject
from Domain.Entities.RaiseObject.Bomb import Bomb
from Domain.Entities.RaiseObject.Gold_Mole import Gold_Mole
from Domain.Entities.RaiseObject.Hacker import Hacker
