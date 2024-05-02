import unittest
import os
import sys

script_dir = os.path.dirname(os.path.relpath(__file__))
sys.path.append(os.path.dirname(script_dir))
from src.is_binary_tree_balanced import is_tree_balanced, BinaryTree


class TestIsTreeBalanced(unittest.TestCase):
    def test_balanced_tree(self):
        root = BinaryTree(3)
        root.left = BinaryTree(6)
        root.right = BinaryTree(4)
        root.left.left = BinaryTree(8)
        root.left.right = BinaryTree(3)
        root.right.left = BinaryTree(5)
        root.right.right = BinaryTree(7)

        self.assertTrue(is_tree_balanced(root))

    def test_unbalanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(5)  
        
        self.assertFalse(is_tree_balanced(root))
      
    def test_empty_tree(self):
        self.assertTrue(is_tree_balanced(None))  
        
    def test_single_node_tree(self):
        root = BinaryTree(1)
        self.assertTrue(is_tree_balanced(root))

    def test_given_tree(self):
        root = BinaryTree(40)
        root.left = BinaryTree(20)
        root.right = BinaryTree(50)
        root.left.left = BinaryTree(5)
        root.left.right = BinaryTree(30)
        root.right.left = BinaryTree(45)
        root.right.right = BinaryTree(60)
        root.left.right.left = BinaryTree(25)
        root.left.right.right = BinaryTree(32)
        root.right.right.right = BinaryTree(55)

        self.assertTrue(is_tree_balanced(root))

if __name__ == "__main__":
    unittest.main()
