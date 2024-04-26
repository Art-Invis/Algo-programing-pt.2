import unittest
from kmp_algorithm import compute_pref_array, search_by_kmp


class TestKMP(unittest.TestCase):
    def test_compute_pref_array(self):
        self.assertEqual(compute_pref_array(""), [0])
        self.assertEqual(compute_pref_array("a"), [0])
        self.assertEqual(compute_pref_array("abcdabca"), [0, 0, 0, 0, 1, 2, 3, 1])

    def test_search_by_kmp(self):
        self.assertEqual(search_by_kmp("banana", ""), [])
        self.assertEqual(search_by_kmp("", "apple"), None)
        self.assertEqual(search_by_kmp("banana", "orange"), None)
        self.assertEqual(search_by_kmp("banana", "na"), [2, 4])
        self.assertEqual(search_by_kmp("mississippi", "issi"), [1, 4])


if __name__ == "__main__":
    unittest.main()
