import unittest
from balanced_tree import is_tree_balanced, BinaryTree


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

if __name__ == "__main__":
    unittest.main()
