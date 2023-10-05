import __init__
import unittest
import sys
from Domain.Entities.mole import mole
from Common.ObjectType import ObjectType


class test_mole(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = 'test'
        print(sys._getframe(0).f_code.co_name)

    @classmethod
    def tearDownClass(cls):
        "Hook method for deconstructing the class fixture after running all tests in the class."
        print(sys._getframe(0).f_code.co_name)

    def setUp(self):
        "Hook method for setting up the test fixture before exercising it."
        print('\t', sys._getframe(0).f_code.co_name)
        self.mole = mole(0, 0, None)

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        print('\t', sys._getframe(0).f_code.co_name)

    def test_start(self):
        print('\t\t', sys._getframe(0).f_code.co_name)
        self.assertTrue(self.mole.state)

    def test_try_lower(self):
        print('\t\t', sys._getframe(0).f_code.co_name)
        self.assertTrue(self.mole.state)
        self.mole.try_lower()
        self.assertFalse(self.mole.state)

    def test_try_attack_1(self):
        print('\t\t', sys._getframe(0).f_code.co_name)
        self.assertTrue(self.mole.state)
        type = self.mole.try_attack()
        self.assertEqual(ObjectType.BASIC_MOLE, type)
        self.assertFalse(self.mole.state)

    def test_try_attack_2(self):
        print('\t\t', sys._getframe(0).f_code.co_name)
        self.assertTrue(self.mole.state)
        print('\t\t\t', "try_attack")
        type = self.mole.try_attack()
        self.assertEqual(ObjectType.BASIC_MOLE, type)
        self.assertFalse(self.mole.state)
        print('\t\t\t', "re try_attack")
        type = self.mole.try_attack()
        self.assertEqual(ObjectType.NONE, type)
        self.assertFalse(self.mole.state)


if __name__ == '__main__':
    unittest.main()
