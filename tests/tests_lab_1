import unittest
from code_lab_1 import is_monotonic


class TestIsMonotonic(unittest.TestCase):

    def test_increasing(self):
        array = [1, 2, 3, 4, 5]
        self.assertTrue(is_monotonic(array))

    def test_decreasing(self):
        array = [5, 4, 3, 2, 1]
        self.assertTrue(is_monotonic(array))

    def test_non_monotonic(self):
        array = [1, 2, 2, 3, 2, 4]
        self.assertFalse(is_monotonic(array))

    def test_empty_array(self):
        array = []
        self.assertTrue(is_monotonic(array))

    def test_single_element(self):
        array = [1]
        self.assertTrue(is_monotonic(array))

    def test_equal_elements(self):
        array = [1, 1, 1, 1]
        self.assertTrue(is_monotonic(array))


if __name__ == "__main__":
    unittest.main()
