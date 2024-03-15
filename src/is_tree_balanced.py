class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_tree_balanced(node: BinaryTree) -> bool:
    is_balanced = True  

    def depth_first_search(node):
        nonlocal is_balanced
        if node is None:
            return 0

        left_subtree = depth_first_search(node.left)
        right_subtree = depth_first_search(node.right)

        if left_subtree is None or right_subtree is None:
            is_balanced = False
        
        height_diff = abs(left_subtree - right_subtree)
        if height_diff > 1:
            is_balanced = False

        if left_subtree > right_subtree :
            return left_subtree + 1
        else:
            return right_subtree + 1

    depth_first_search(node)  

    return is_balanced
