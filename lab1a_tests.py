# Melissa Melton
# CPE 202 Lab 1 Test Cases

import unittest
from lab1a import *

class TestLab1(unittest.TestCase):

    def test_max_list_01(self) -> None:
        # checks that max number is returned from list of multiple numbers
        tlist = [1,2,3]
        self.assertEqual(max_list_iter(tlist),3)

    def test_max_list_02(self) -> None:
        # used to check for exception
        tlist = None
        with self.assertRaises(ValueError):
            max_list_iter(tlist)

    def test_max_list_03(self) -> None:
        # checks that entering an empty list returns None
        tlist: List[int] = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_max_list_04(self) -> None:
        # checks that entering an empty list returns None
        tlist = [20]
        self.assertEqual(max_list_iter(tlist), 20)

    def test_reverse_01(self) -> None:
        # checks that list is reversed
        intlist: List[int] = [1,2,3]
        revlist: Optional[List[any]] = reverse_list(intlist)
        self.assertEqual(revlist,[3,2,1])
        self.assertEqual(intlist,[1,2,3])

    def test_reverse_02(self) -> None:
        # checks that an empty list is returned if an empty list was entered
        intList: List[int] = []
        revList: List[int] = []
        self.assertEqual(revList, reverse_list(intList))

    def test_reverse_03(self) -> None:
        # additional check for whether list is reversed. Assert true and assert equal
        intList: List[int] = [8, 10, 5, 0]
        revList: List[int] = [0, 5, 10, 8]
        revList2 = reverse_list(intList)
        self.assertTrue(revList == revList2)
        self.assertEqual(revList, reverse_list(intList))

    def test_reverse_04(self) -> None:
        # checks that same list of length 1 is returned if list of length 1 is entered
        intList: List[int] = [901]
        revList: List[int] = [901]
        self.assertEqual(reverse_list(intList), revList)

    def test_reverse_05(self) -> None:
        # used to check for exception
        intList = None
        with self.assertRaises(ValueError):
            reverse_list(intList)

    def test_reverse_mutate_01(self) -> None:
        # checks that a list of multiple numbers is reversed
        intlist: List[int] = [1,2,3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist,[3,2,1])

    def test_reverse_mutate_02(self) -> None:
        # checks that an empty list is returned if empty list is entered
        intlist: List[int] = []
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [])

    def test_reverse_mutate_03(self) -> None:
        # used to check for exception
        intList = None
        with self.assertRaises(ValueError):
            reverse_list_mutate(intList)


if __name__ == "__main__":
        unittest.main()