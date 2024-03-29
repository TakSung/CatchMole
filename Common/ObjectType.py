from enum import IntEnum


class ObjectType(IntEnum):
    none = 0
    BASIC_MOLE = 1
    HACKER = 2
    BOMB = 3
    GOLD_MOLE = 4
    RED_BOMB = 5


def get_object_type(i: int) -> ObjectType:
    for member in ObjectType:
        if i == int(member):
            return member
    return ObjectType.none
