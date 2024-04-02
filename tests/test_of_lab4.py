import unittest
from red_black_priority_queue import RedBlackTree


class TestRedBlackTree(unittest.TestCase):

    def test_peek_sequence(self):
        tree = RedBlackTree()
        tree.insert(9, 5)
        tree.insert(7, 6)
        tree.insert(4, 7)
        tree.insert(8, 3)
        tree.insert(5, 9)
        tree.insert(3, 8)
        tree.insert(2, 4)
        self.assertEqual(tree.delete_max(), (5, 9))
        self.assertEqual(tree.view_queue(), [(3, 8), (7, 6), (9, 5), (2, 4), (8, 3)])


if __name__ == "__main__":
    unittest.main()
