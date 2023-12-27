import sys
from pathlib import Path

now_path = Path(__file__).parent
root_path = str(now_path.parent.parent)

if not (root_path in sys.path):
    sys.path.append(root_path)


from Application.GameManage.PlayerActionSet import PlayerActionSet
from Application.GameManage.PlayerManager import PlayerManager
from  Application.GameManage.IConvertObjectToState import IConvertObjectToState