class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def depth_first_search(node):
        if node is None:
            return True, 0

        left_subtree = depth_first_search(node.left)
        right_subtree = depth_first_search(node.right)

        l_balance, left_height = left_subtree
        r_balance, right_height = right_subtree

        if abs(left_height - right_height) <= 1:
            height_diff = True
        else:
            height_diff = False
            
        height = max(left_height, right_height) + 1

        if l_balance and r_balance and height_diff:
            return True, height  
        else:
            return False, height

def is_tree_balanced(node: BinaryTree) -> bool:
    is_balanced = depth_first_search(node)[0]

    return is_balanced
