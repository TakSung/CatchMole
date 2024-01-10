import __init__
import unittest
import sys
from Common.ObjectType import *


class test_object_type(unittest.TestCase):
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

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        print("\t", sys._getframe(0).f_code.co_name)

    def test_start(self):
        print("\t\t", sys._getframe(0).f_code.co_name)
        type = get_object_type(0)
        self.assertEqual(ObjectType.none, type)
        type = get_object_type(1)
        self.assertEqual(ObjectType.BASIC_MOLE, type)


if __name__ == "__main__":
    unittest.main()
