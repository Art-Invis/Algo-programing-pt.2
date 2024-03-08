import unittest

from Lab2_3 import binary_min_length_search


class TestMinimalBoardLength(unittest.TestCase):
    def test_given_values(self):
        self.assertEqual(binary_min_length_search(10, 2, 3), 9)
        self.assertEqual(binary_min_length_search(2, 1000000000, 999999999), 1999999998)
        self.assertEqual(binary_min_length_search(4, 1, 1), 2)

    def test_values_equal_zero(self):
        self.assertEqual(binary_min_length_search(0, 6, 18), None)
        self.assertEqual(binary_min_length_search(4, 0, 35), None)
        self.assertEqual(binary_min_length_search(8, 5, 0), None)


if __name__ == "__main__":
    unittest.main()
