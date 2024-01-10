import __init__
import unittest
import sys
from icecream import ic

from Common import PlayerState, ObjectType
from Domain.Entities.Cursor import Cursor
from Domain.Entities import RaiseHole, TestObjFactory
from Application.GameManage import PlayerActor, OneBoardGameManager
from Application.StateFilter import BuffFilter, DebuffFilter

from Tests.Application.StateFilter import TestHackerBoard


class test_player_filter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = "test"
        print(sys._getframe(0).f_code.co_name, "test_player_filter")

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
            board=TestHackerBoard(),
            player_num=1,
            buff_filter=debuff,
            debuff_filter=debuff,
        )
        self.player = self.manager.player_list[0]
        self.cursor = self.player.cursor

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t", sys._getframe(0).f_code.co_name)

    def test_반전_시간지나서_정상(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t\t", sys._getframe(0).f_code.co_name)
        hacker = self.player.try_attack()
        self.assertEqual(ObjectType.HACKER, hacker)

        self.player.right()
        self.assertEqual((0, 0), self.cursor.get())

        self.player.left()
        self.assertEqual((0, 1), self.cursor.get())
        self.player.left()
        self.assertEqual((0, 2), self.cursor.get())
        self.player.left()
        self.assertEqual((0, 3), self.cursor.get())
        self.player.left()
        self.assertEqual((0, 4), self.cursor.get())
        self.player.left()
        self.assertEqual((0, 4), self.cursor.get())

        self.player.up()
        self.assertEqual((0, 4), self.cursor.get())

        self.player.down()
        self.assertEqual((1, 4), self.cursor.get())
        self.player.down()
        self.assertEqual((2, 4), self.cursor.get())
        self.player.down()
        self.assertEqual((3, 4), self.cursor.get())
        self.player.down()
        self.assertEqual((4, 4), self.cursor.get())
        self.player.down()
        self.assertEqual((4, 4), self.cursor.get())

        self.player.left()
        self.assertEqual((4, 4), self.cursor.get())

        # Nomal
        import time

        time.sleep(self.time)
        self.cursor.set(0, 0)
        self.assertEqual((0, 0), self.cursor.get())

        self.player.left()
        self.assertEqual((0, 0), self.cursor.get())

        self.player.right()
        self.assertEqual((0, 1), self.cursor.get())

        self.player.right()
        self.assertEqual((0, 2), self.cursor.get())

        self.player.right()
        self.assertEqual((0, 3), self.cursor.get())

        self.player.right()
        self.assertEqual((0, 4), self.cursor.get())

        self.player.right()
        self.assertEqual((0, 4), self.cursor.get())

        self.player.down()
        self.assertEqual((0, 4), self.cursor.get())

        self.player.up()
        self.assertEqual((1, 4), self.cursor.get())
        self.player.up()
        self.assertEqual((2, 4), self.cursor.get())
        self.player.up()
        self.assertEqual((3, 4), self.cursor.get())
        self.player.up()
        self.assertEqual((4, 4), self.cursor.get())
        self.player.up()
        self.assertEqual((4, 4), self.cursor.get())
        self.player.right()
        self.assertEqual((4, 4), self.cursor.get())

    def test_반전(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t\t", sys._getframe(0).f_code.co_name)
        hacker = self.player.try_attack()
        self.assertEqual(ObjectType.HACKER, hacker)

        self.player.right()
        self.assertEqual((0, 0), self.cursor.get())

        self.player.left()
        self.assertEqual((0, 1), self.cursor.get())
        self.player.left()
        self.assertEqual((0, 2), self.cursor.get())
        self.player.left()
        self.assertEqual((0, 3), self.cursor.get())
        self.player.left()
        self.assertEqual((0, 4), self.cursor.get())
        self.player.left()
        self.assertEqual((0, 4), self.cursor.get())

        self.player.up()
        self.assertEqual((0, 4), self.cursor.get())

        self.player.down()
        self.assertEqual((1, 4), self.cursor.get())
        self.player.down()
        self.assertEqual((2, 4), self.cursor.get())
        self.player.down()
        self.assertEqual((3, 4), self.cursor.get())
        self.player.down()
        self.assertEqual((4, 4), self.cursor.get())
        self.player.down()
        self.assertEqual((4, 4), self.cursor.get())

        self.player.left()
        self.assertEqual((4, 4), self.cursor.get())


if __name__ == "__main__":
    unittest.main()
