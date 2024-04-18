import unittest
from min_num_of_beers import make_matrix_of_preferences

class MinNumOfBeer(unittest.TestCase):
    def test_given_value(self):
        self.assertEqual(make_matrix_of_preferences(2, 2, 'YN NY'), 2)
        self.assertEqual(make_matrix_of_preferences(6, 3, 'YNN YNY YNY NYY NYY NYN'), 2)

    def test_do_not_like_any_beer(self):
        self.assertEqual(make_matrix_of_preferences(5, 2, 'NN NN NN NN'), 0)

    def test_same_preferences(self):
        self.assertEqual(make_matrix_of_preferences(5, 2, 'NY NY NY NY NY '), 1)

    def test_only_one_preference_is_same(self):
        self.assertEqual(make_matrix_of_preferences(4, 4, 'NYNY YNNY NNYY YNYY'), 1)

    def test_every_preference_is_unique(self):
        self.assertEqual(make_matrix_of_preferences(5, 5, 'NNNNY NNNYN NNYNN NYNNN YNNNN'), 5)

if __name__ == '__main__':
    unittest.main()