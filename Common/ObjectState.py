from enum import IntEnum


class ObjectState(IntEnum):
    NONE = 0
    RAISE_OBJECT = 1
    CATCHED = 2
    LOW = 3


def get_object_type(i: int) -> ObjectState:
    for member in ObjectState:
        if i == int(member):
            return member
    return ObjectState.NONE
