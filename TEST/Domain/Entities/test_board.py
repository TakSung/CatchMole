import __init__
import unittest
import sys
import time
import random
from icecream import ic

from Common.ObjectType import ObjectType
from Domain.Interfaces.IRaiseObj import IRaiseObj
from Domain.Entities.ObjFactory import *
from Domain.Entities.MoleBoard import MoleBoard


class test_mole(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = 'test'
        print(sys._getframe(0).f_code.co_name)
        ic.disable()

    @classmethod
    def tearDownClass(cls):
        "Hook method for deconstructing the class fixture after running all tests in the class."
        print(sys._getframe(0).f_code.co_name)

    def setUp(self):
        "Hook method for setting up the test fixture before exercising it."
        print('\t', sys._getframe(0).f_code.co_name)
        self.timer = 0.101
        self.mole_board = MoleBoard(factory=TestObjFactory())

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        print('\t', sys._getframe(0).f_code.co_name)

    def test_start(self):
        print('\t\t', sys._getframe(0).f_code.co_name)
        self.assertEqual(MoleBoard.empty_board_state(),
                         self.mole_board.get_board_state())
        self.assertEqual(MoleBoard.empty_board_state(),
                         self.mole_board.get_board_state())

    def test_raise_obj_1(self):
        print('\t\t', sys._getframe(0).f_code.co_name)

        mp = MoleBoard.empty_board_state()
        self.assertEqual(mp, self.mole_board.get_board_state())

        self.mole_board.raise_obj(0, 0, ObjectType.BASIC_MOLE)
        mp[0][0] = ObjectType.BASIC_MOLE
        self.assertEqual(mp, self.mole_board.get_board_state())


        time.sleep(self.timer + 0.001)
        self.assertEqual(MoleBoard.empty_board_state(), 
                         self.mole_board.get_board_state())

    def test_raise_obj_2(self):
        print('\t\t', sys._getframe(0).f_code.co_name)
        mp = MoleBoard.empty_board_state()
        self.assertEqual(mp, self.mole_board.get_board_state())

        mole = self.mole_board.raise_obj(0, 0, ObjectType.BASIC_MOLE)
        mp[0][0] = ObjectType.BASIC_MOLE
        self.assertEqual(mp, self.mole_board.get_board_state())

        result = mole.try_attack()
        self.assertEqual(MoleBoard.empty_board_state(),
                         self.mole_board.get_board_state())
        self.assertEqual(ObjectType.BASIC_MOLE, result)


if __name__ == '__main__':
    unittest.main()
