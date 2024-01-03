import __init__
import unittest
import sys
from icecream import ic

from Common import PlayerState
from Domain.Entities.Cursor import Cursor
from Domain.Entities import RaiseHole, TestObjFactory
from Application.GameManage import PlayerActionSet
from Application.StateFilter import PlayerEventDefinder, BuffFilter, DebuffFilter


class test_player_action_set(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = "test"
        print(sys._getframe(0).f_code.co_name)

    @classmethod
    def tearDownClass(cls):
        "Hook method for deconstructing the class fixture after running all tests in the class."
        print(sys._getframe(0).f_code.co_name)

    def setUp(self):
        "Hook method for setting up the test fixture before exercising it."
        print("\t", sys._getframe(0).f_code.co_name)
        self.player = PlayerActionSet(5)
        self.cursor = self.player.cursor
        self.hole = RaiseHole(1, 1, factory=TestObjFactory(0.5))

        buff = BuffFilter()
        debuff = DebuffFilter(1)

        PlayerEventDefinder(
            trigger_matchs=[
                ([self.player], self.hole, debuff),
                ([self.player], self.hole, buff),
            ]
        )

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t", sys._getframe(0).f_code.co_name)

    def test__반전(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t\t", sys._getframe(0).f_code.co_name)
        self.player.update_state(PlayerState.Reverse)

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

    def test_이상한움직임들(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t\t", sys._getframe(0).f_code.co_name)

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

    def test_start(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t\t", sys._getframe(0).f_code.co_name)
        self.assertEqual((0, 0), self.cursor.get())

        self.player.right()
        self.assertEqual((0, 1), self.cursor.get())

        self.player.left()
        self.assertEqual((0, 0), self.cursor.get())

        self.player.up()
        self.assertEqual((1, 0), self.cursor.get())

        self.player.down()
        self.assertEqual((0, 0), self.cursor.get())


if __name__ == "__main__":
    unittest.main()
