# CPE 202 Lab 1 Test Cases

import unittest
from lab1a import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_01(self) -> None:
        tlist = [1,2,3]
        self.assertEqual(max_list_iter(tlist),3)

    def test_max_list_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_01(self) -> None:
        intlist = [1,2,3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist,[3,2,1])
        self.assertEqual(intlist,[1,2,3])

    def test_reverse_02(self) -> None:
        intList = []
        revList = []
        self.assertEqual(revList, reverse_list(intList))

    def test_reverse_03(self) -> None:
        intList = [8, 10, 5, 0]
        revList = [0, 5, 10, 8]
        revList2 = reverse_list(intList)
        self.assertTrue(revList == revList2)
        self.assertEqual(revList, reverse_list(intList))

    def test_reverse_04(self) -> None:
        intList = [901]
        revList = [901]
        self.assertEqual(reverse_list(intList), revList)

    def test_reverse_05(self) -> None:
        intList = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_list(intList)

    def test_reverse_mutate(self) -> None:
        intlist = [1,2,3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist,[3,2,1])

    def test_reverse_mutate_1(self) -> None:
        intlist = [1,2,3]
        self.assertEqual(reverse_list_mutate(intlist), None)

    def test_reverse_mutate_02(self) -> None:
        intList = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_list_mutate(intList)

if __name__ == "__main__":
        unittest.main()