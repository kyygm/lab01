import unittest

from hypothesis import given
import hypothesis.strategies as st

from UnrolledLinkedList import *


class MyTestCase(unittest.TestCase):
    def test_size(self):
        self.assertEqual(UnrolledLinkedList(5).size(), 0)
        self.assertEqual(UnrolledLinkedList(5).add(1).size(), 1)
        self.assertEqual(UnrolledLinkedList(5).add(1).add(2).add(3).add(4)
                         .add(5).add(6).add(7).size(), 7)

    def test_to_list(self):
        self.assertEqual(UnrolledLinkedList(5).to_list(), [])
        self.assertEqual(UnrolledLinkedList(5).add(1).add(2).add(3).to_list(), [1, 2, 3])

    def test_from_list(self):
        test_data = [
            [],
            [1, 2],
            [1, 2, 3, 4, 5, 6, 7]
        ]
        for e in test_data:
            lst = UnrolledLinkedList(5)
            self.assertEqual(lst.from_list(e).to_list(), e)
            self.assertEqual(lst.to_list(), [])

    def test_add(self):
        lst = UnrolledLinkedList(5).add(1).add(2).add(3)
        lst.add(4)
        self.assertEqual(lst.to_list(), [1, 2, 3])
        self.assertEqual(lst.add(4).to_list(), [1, 2, 3, 4])

    def test_remove(self):
        lst = UnrolledLinkedList(5).add(1).add(2).add(3)
        lst.remove(1)
        self.assertEqual(lst.to_list(), [1, 2, 3])
        self.assertEqual(lst.remove(1).to_list(), [2, 3])

    def test_reverse(self):
        lst = UnrolledLinkedList(5).add(1).add(2).add(3)
        lst.reverse()
        self.assertEqual(lst.to_list(), [1, 2, 3])
        self.assertEqual(lst.reverse().to_list(), [3, 2, 1])

    def test_map(self):
        lst = UnrolledLinkedList(5).add(1).add(2).add(3)
        lst.map(str)
        self.assertEqual(lst.to_list(), [1, 2, 3])
        self.assertEqual(lst.map(str).to_list(), ['1', '2', '3'])

        lst.map(lambda x: x + 1)
        self.assertEqual(lst.to_list(), [1, 2, 3])
        self.assertEqual(lst.map(lambda x: x + 1).to_list(), [2, 3, 4])

    def test_reduce(self):
        lst = UnrolledLinkedList(5)
        self.assertEqual(lst.reduce(lambda state, e: state + e, 0), 0)
        self.assertEqual(lst.reduce(lambda state, e: state + e, 1), 1)

        self.assertEqual(lst.from_list([1, 2, 3]).reduce(lambda state, e: state + e, 0), 6)

    def test_get(self):
        self.assertRaises(IndexError, lambda: UnrolledLinkedList(5).add(1).get(1))
        self.assertEqual(UnrolledLinkedList(5).add(1).add(2).add(3).get(2), 3)

    def test_iter(self):
        lst = UnrolledLinkedList(5).add(1).add(2).add(3).add(4).add(5).add(6).add(7)
        lst2 = []
        for n in lst:
            try:
                lst2.append(n)
            except StopIteration:
                pass
        self.assertEqual(lst2, [1, 2, 3, 4, 5, 6, 7])

    def test_mconcat(self):
        lst1 = UnrolledLinkedList(5).add(1).add(2).add(3)
        lst2 = UnrolledLinkedList(5).add(4).add(5).add(6).add(7)
        lst1.mconcat(lst2)
        lst3 = UnrolledLinkedList(5).add(1).add(2).add(3).add(4).add(5).add(6).add(7)
        self.assertEqual(lst1.to_list(), [1, 2, 3])
        self.assertEqual(lst1.mconcat(lst2).to_list(), lst3.to_list())

    def test_find(self):
        lst = UnrolledLinkedList(5)
        self.assertEqual(lst.find(2), False)
        lst = UnrolledLinkedList(5).add(1).add(2).add(3)
        self.assertEqual(lst.find(2), True)
        self.assertEqual(lst.find(4), False)

    def test_set(self):
        lst = UnrolledLinkedList(5).add(1).add(2).add(3)
    #   self.assertRaises(IndexError, lambda: lst.set(0, 1))
        lst.set(1, 5)
        self.assertEqual(lst.to_list(), [1, 2, 3])
        self.assertEqual(lst.set(1, 5).to_list(), [1, 5, 3])

    def test_filter(self):
        lst = UnrolledLinkedList(5).add(1).add(2).add(3)

        def is_even(n):
            return n % 2 == 0
        lst.filter(is_even)
        self.assertEqual(lst.to_list(), [1, 2, 3])
        self.assertEqual(lst.filter(is_even).to_list(), [2])


if __name__ == '__main__':
    unittest.main()
