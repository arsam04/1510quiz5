import unittest
from sorted import is_sorted

unsorted_list = [3, 2, 5]
sorted_list = [1, 2, 3]


class Test(unittest.TestCase):
    def test_sorted(self):
        self.AssertTrue(is_sorted(sorted_list))

    def test_unsorted(self):
        self.assertFalse(is_sorted(unsorted_list))

    def test_empty(self):



