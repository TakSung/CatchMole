import __init__
import unittest
import sys
import threading
import time
import random
from icecream import ic

from Domain.Entities.RaiseHole import RaiseHole
from Domain.Entities.MoleBoard import MoleBoard
from Domain.Entities.ObjFactory import *
from Common.ObjectType import ObjectType


class test_mole(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = "test"
        print(sys._getframe(0).f_code.co_name)
        ic.disable()

    @classmethod
    def tearDownClass(cls):
        "Hook method for deconstructing the class fixture after running all tests in the class."
        print(sys._getframe(0).f_code.co_name)

    def setUp(self):
        "Hook method for setting up the test fixture before exercising it."
        print("\t", sys._getframe(0).f_code.co_name)
        self.mole_board = MoleBoard()
        self.timer = 0.1
        self.mole = RaiseHole(0, 0, [self.mole_board], TestObjFactory())
        self.mole.set_raise_object_to_type(ObjectType.BASIC_MOLE)
        # self.mole = NoneObject()
        self.mole_board.set_obj(0, 0, self.mole)

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t", sys._getframe(0).f_code.co_name)

    def test_start(self):
        print("\t\t", sys._getframe(0).f_code.co_name)
        TYPE = self.mole.get_state()
        self.assertEqual(TYPE, self.mole_board.get_state(0, 0))

    def test_try_lower(self):
        print("\t\t", sys._getframe(0).f_code.co_name)
        TYPE = self.mole.get_state()
        self.assertEqual(TYPE, self.mole_board.get_state(0, 0))

        self.mole.try_lower()
        self.assertEqual(ObjectType.NONE, self.mole_board.get_state(0, 0))

    def test_try_attack_1(self):
        print("\t\t", sys._getframe(0).f_code.co_name)
        TYPE = self.mole.get_state()
        self.assertEqual(TYPE, self.mole_board.get_state(0, 0))

        type = self.mole.try_attack()
        self.assertEqual(ObjectType.BASIC_MOLE, type)
        self.assertEqual(ObjectType.NONE, self.mole_board.get_state(0, 0))

    def test_try_attack_2(self):
        from icecream import ic
        print("\t\t", sys._getframe(0).f_code.co_name)
        TYPE = self.mole.get_state()
        self.assertEqual(TYPE, self.mole_board.get_state(0, 0))

        print("\t\t\t", "try_attack")
        ic(self.mole, self.mole.get_state())
        type = self.mole.try_attack()
        self.assertEqual(ObjectType.BASIC_MOLE, type)
        print("\t\t\t", "re try_attack")
        type = self.mole.try_attack()
        self.assertEqual(ObjectType.NONE, type)
        self.assertEqual(ObjectType.NONE, self.mole_board.get_state(0, 0))

    def test_auto_lower(self):
        print("\t\t", sys._getframe(0).f_code.co_name)
        TYPE = self.mole.get_state()
        MAX = 10
        queue = []
        theads = []
        results = [ObjectType.NONE] * MAX

        def attack(id: int):
            time.sleep(random.randint(0, 3) * 0.0001)
            queue.append(id)
            results[id] = self.mole.try_attack()

        for i in range(MAX):
            theads.append(threading.Thread(target=attack, args=(i,)))
        time.sleep(self.timer)

        for i in range(MAX):
            theads[i].start()

        for i in range(MAX):
            theads[i].join()
        self.assertEqual(set([ObjectType.NONE]), set(results))
        self.assertEqual(ObjectType.NONE, self.mole_board.get_state(0, 0))

    def test_threading_try_attack_1(self):
        print("\t\t", sys._getframe(0).f_code.co_name)
        TYPE = self.mole.get_state()
        MAX = 10
        queue = []
        theads = []
        results = [ObjectType.NONE] * MAX

        def attack(id: int):
            time.sleep(random.randint(0, 3) * 0.001)
            queue.append(id)
            results[id] = self.mole.try_attack()

        for i in range(MAX):
            theads.append(threading.Thread(target=attack, args=(i,)))

        for i in range(MAX):
            theads[i].start()

        for i in range(MAX):
            theads[i].join()
        self.assertEqual(TYPE, results[queue[0]])
        results[queue[0]] = ObjectType.NONE
        self.assertEqual(set([ObjectType.NONE]), set(results))
        self.assertEqual(ObjectType.NONE, self.mole_board.get_state(0, 0))

    def test_threading_try_attack_2(self):
        print("\t\t", sys._getframe(0).f_code.co_name)
        TYPE = self.mole.get_state()
        MAX = 10
        queue = []
        theads = []
        results = [ObjectType.NONE] * MAX

        def attack_or_lower(id: int):
            if id == -1:
                time.sleep(0.003)
            else:
                time.sleep(random.randint(0, 3) * 0.00001)
            queue.append(id)
            if id == -1:
                self.mole.try_lower()
            else:
                results[id] = self.mole.try_attack()

        for i in range(MAX + 1):
            theads.append(threading.Thread(target=attack_or_lower, args=((i - 1),)))

        for i in range(MAX):
            theads[i].start()

        for i in range(MAX):
            theads[i].join()

        frist = queue[0]
        if frist >= 0:
            self.assertEqual(TYPE, results[frist])
            results[queue[0]] = ObjectType.NONE
        self.assertEqual(set([ObjectType.NONE]), set(results))
        self.assertEqual(ObjectType.NONE, self.mole_board.get_state(0, 0))

    def test_threading_try_attack_3(self):
        print("\t\t", sys._getframe(0).f_code.co_name)
        TYPE = self.mole.get_state()
        MAX = 10
        queue = []
        theads = []
        results = [ObjectType.NONE] * MAX

        def attack_or_lower(id: int):
            if id != -1:
                time.sleep(random.randint(0, 3) * 0.00001)
            queue.append(id)
            if id == -1:
                self.mole.try_lower()
            else:
                results[id] = self.mole.try_attack()

        for i in range(MAX + 1):
            theads.append(threading.Thread(target=attack_or_lower, args=((i - 1),)))

        for i in range(MAX):
            theads[i].start()

        for i in range(MAX):
            theads[i].join()

        frist = queue[0]
        if frist >= 0:
            self.assertEqual(TYPE, results[frist])
            results[queue[0]] = ObjectType.NONE
        self.assertEqual(set([ObjectType.NONE]), set(results))
        self.assertEqual(ObjectType.NONE, self.mole_board.get_state(0, 0))


if __name__ == "__main__":
    unittest.main()
