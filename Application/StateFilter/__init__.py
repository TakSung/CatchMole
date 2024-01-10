import sys
from pathlib import Path

now_path = Path(__file__).parent
root_path = str(now_path.parent.parent)

if not (root_path in sys.path):
    sys.path.append(root_path)


from Application.StateFilter.IConvertObjectToState import IConvertObjectToState
from Application.StateFilter.ObjectPlayerLinker import ObjectPlayerLinker
from Application.StateFilter.BaseFilter import BuffFilter, DebuffFilter
