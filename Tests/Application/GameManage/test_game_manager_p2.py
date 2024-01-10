import __init__
import unittest
import sys
from icecream import ic

from Common import PlayerState
from Domain.Entities.Cursor import Cursor
from Application.GameManage import PlayerCursorControl

from Common import PlayerState, ObjectType
from Domain.Entities.Cursor import Cursor
from Application.GameManage import PlayerActor, OneBoardGameManager
from Application.StateFilter import BuffFilter, DebuffFilter

from Tests.Application.GameManage import TestHalfHackerBoard


class test_game_manager_p2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = "test"
        print(sys._getframe(0).f_code.co_name, "test_game_manager_p2")

    @classmethod
    def tearDownClass(cls):
        "Hook method for deconstructing the class fixture after running all tests in the class."
        print(sys._getframe(0).f_code.co_name)

    def setUp(self):
        "Hook method for setting up the test fixture before exercising it."
        print("\t", sys._getframe(0).f_code.co_name)
        self.time = 1
        debuff = DebuffFilter(self.time)
        self.manager = OneBoardGameManager(
            board=TestHalfHackerBoard(),
            player_num=2,
            debuff_filter=debuff,
        )
        self.player1 = self.manager.player_list[0]
        self.player2 = self.manager.player_list[1]
        self.cursor1 = self.player1.cursor
        self.cursor2 = self.player2.cursor

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t", sys._getframe(0).f_code.co_name)

    def test_p1_반전_p2의_공격(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t\t", sys._getframe(0).f_code.co_name)
        self.player1.update_state(PlayerState.Reverse)

        self.player1.right()
        self.assertEqual((0, 0), self.cursor1.get())

        self.player1.left()
        self.assertEqual((0, 1), self.cursor1.get())
        self.player1.left()
        self.assertEqual((0, 2), self.cursor1.get())
        self.player1.left()
        self.assertEqual((0, 3), self.cursor1.get())
        self.player1.left()
        self.assertEqual((0, 4), self.cursor1.get())
        self.player1.left()
        self.assertEqual((0, 4), self.cursor1.get())

        self.player1.up()
        self.assertEqual((0, 4), self.cursor1.get())

        self.player1.down()
        self.assertEqual((1, 4), self.cursor1.get())
        self.player1.down()
        self.assertEqual((2, 4), self.cursor1.get())
        self.player1.down()
        self.assertEqual((3, 4), self.cursor1.get())
        self.player1.down()
        self.assertEqual((4, 4), self.cursor1.get())
        self.player1.down()
        self.assertEqual((4, 4), self.cursor1.get())

        self.player1.left()
        self.assertEqual((4, 4), self.cursor1.get())

    def test_p1_반전(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t\t", sys._getframe(0).f_code.co_name)
        self.player1.update_state(PlayerState.Reverse)

        self.player1.right()
        self.assertEqual((0, 0), self.cursor1.get())

        self.player1.left()
        self.assertEqual((0, 1), self.cursor1.get())
        self.player1.left()
        self.assertEqual((0, 2), self.cursor1.get())
        self.player1.left()
        self.assertEqual((0, 3), self.cursor1.get())
        self.player1.left()
        self.assertEqual((0, 4), self.cursor1.get())
        self.player1.left()
        self.assertEqual((0, 4), self.cursor1.get())

        self.player1.up()
        self.assertEqual((0, 4), self.cursor1.get())

        self.player1.down()
        self.assertEqual((1, 4), self.cursor1.get())
        self.player1.down()
        self.assertEqual((2, 4), self.cursor1.get())
        self.player1.down()
        self.assertEqual((3, 4), self.cursor1.get())
        self.player1.down()
        self.assertEqual((4, 4), self.cursor1.get())
        self.player1.down()
        self.assertEqual((4, 4), self.cursor1.get())

        self.player1.left()
        self.assertEqual((4, 4), self.cursor1.get())

    def test_p1_이상한움직임들(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t\t", sys._getframe(0).f_code.co_name)

        self.player1.left()
        self.assertEqual((0, 0), self.cursor1.get())

        self.player1.right()
        self.assertEqual((0, 1), self.cursor1.get())

        self.player1.right()
        self.assertEqual((0, 2), self.cursor1.get())

        self.player1.right()
        self.assertEqual((0, 3), self.cursor1.get())

        self.player1.right()
        self.assertEqual((0, 4), self.cursor1.get())

        self.player1.right()
        self.assertEqual((0, 4), self.cursor1.get())

        self.player1.down()
        self.assertEqual((0, 4), self.cursor1.get())

        self.player1.up()
        self.assertEqual((1, 4), self.cursor1.get())
        self.player1.up()
        self.assertEqual((2, 4), self.cursor1.get())
        self.player1.up()
        self.assertEqual((3, 4), self.cursor1.get())
        self.player1.up()
        self.assertEqual((4, 4), self.cursor1.get())
        self.player1.up()
        self.assertEqual((4, 4), self.cursor1.get())
        self.player1.right()
        self.assertEqual((4, 4), self.cursor1.get())


if __name__ == "__main__":
    unittest.main()
