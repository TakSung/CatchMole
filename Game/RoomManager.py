import __init__
from abc import *
from typing import Tuple, List
from collections.abc import Collection

from Domain.Interfaces.IBoardObserver import IBoardObserver
from Common.ObjectType import ObjectType

from Domain.Entities.MoleBoard import MoleBoard
from Application.GameManage import PlayerActor


class GUIRoom:
    """_summary_
    1. 라이즈홀에 객체 관리
    2. 커서 관리
    3. 변경사항 관리
    4. 현재 자신의 위치 관리
    5. 이펙트 관리(차후 진행)
    """

    def __init__(self, y: int, x: int, player_num: int = 1):
        self.y, self.x = y, x
        self.change = True
        self.cursors = [False for _ in range(player_num)]
        self.obj = ObjectType.none

    def set_cursor(self, on: bool, idx: int = 0):
        assert idx >= 0 and idx < len(self.cursors)
        self.cursors[idx] = on
        self.change = True

    def set_obj(self, obj: ObjectType):
        self.obj = obj
        self.change = True

    def is_change(self) -> bool:
        return self.change

    def check_room(self):
        self.change = False

    def check_and_get_room(self) -> Tuple[int, int, ObjectType, bool]:
        """_summary_
        룸에 있는 정보들을 튜플형태로 얻는다.
        y,x위치, 룸의 존재하는 객체 종류, 커서의 존재여부

        Returns:
            Tuple[int, int, ObjectType, bool]: _description_ y, x, object_type, is_cursor
        """
        self.check_room()
        return self.get_room()

    def get_room(self) -> Tuple[int, int, ObjectType, List[bool]]:
        """_summary_
        룸에 있는 정보들을 튜플형태로 얻는다. 순서는 반환 주석을 참고 하라
        y,x위치, 룸의 존재하는 객체 종류, 커서의 존재여부

        Returns:
            Tuple[int, int, ObjectType, bool]: _description_ y, x, object_type, is_cursor
        """
        return (self.y, self.x, self.obj, self.cursors)


class RoomManager:
    def __init__(self, size: int = 3):
        self.size = size
        self.rooms = [[GUIRoom(y, x) for x in range(size)] for y in range(size)]
        self.cursor_x, self.cursor_y = 0, 0
        self.set_cursor(0, 0)

    def set_cursor(self, y: int, x: int):
        self.rooms[self.cursor_y][self.cursor_x].set_cursor(False)
        self.cursor_x, self.cursor_y = x, y
        self.rooms[y][x].set_cursor(True)

    def set_obj(self, y: int, x: int, type: ObjectType):
        self.rooms[y][x].set_obj(type)

    def get_changed_list(self) -> List[Tuple[int, int, ObjectType, List[bool]]]:
        """_summary_
        룸에 있는 정보들을 튜플형태로 얻는다.
        y,x위치, 룸의 존재하는 객체 종류, 커서의 존재여부

        Returns:
            List[Tuple[int, int, ObjectType, bool]]: _description_ y, x, object_type, is_cursor
        """
        changed_list = [
            (self.rooms[y][x].get_room())
            for y in range(self.size)
            for x in range(self.size)
            if self.rooms[y][x].is_change()
        ]
        return changed_list

    def check_room(self):
        for y in range(self.size):
            for x in range(self.size):
                self.rooms[y][x].check_room()


#


class RoomManagerP2:
    def __init__(self, size: int = 3):
        self.size = size
        self.rooms = [[GUIRoom(y, x) for x in range(size)] for y in range(size)]
        self.cursor_x, self.cursor_y = 0, 0

    def set_cursor(
        self,
        y: int,
        x: int,
    ):
        self.rooms[self.cursor_y][self.cursor_x].set_cursor(False)
        self.cursor_x, self.cursor_y = x, y
        self.rooms[y][x].set_cursor(True)

    def set_obj(self, y: int, x: int, type: ObjectType):
        self.rooms[y][x].set_obj(type)

    def get_changed_list(self) -> List[Tuple[int, int, ObjectType, bool]]:
        """_summary_
        룸에 있는 정보들을 튜플형태로 얻는다.
        y,x위치, 룸의 존재하는 객체 종류, 커서의 존재여부

        Returns:
            List[Tuple[int, int, ObjectType, bool]]: _description_ y, x, object_type, is_cursor
        """
        changed_list = [
            (self.rooms[y][x].get_room())
            for y in range(self.size)
            for x in range(self.size)
            if self.rooms[y][x].is_change()
        ]
        return changed_list

    def check_room(self):
        for y in range(self.size):
            for x in range(self.size):
                self.rooms[y][x].check_room()
