from enum import IntEnum


class ObjectType(IntEnum):
    NONE = 0
    BASIC_MOLE = 1
    HACKER = 2
    BOMB = 3
    GOLD_MOLE = 4

def get_object_type(i:int) -> ObjectType:
    for member in ObjectType:
        if i == int(member):
            return member
    return ObjectType.NONE



