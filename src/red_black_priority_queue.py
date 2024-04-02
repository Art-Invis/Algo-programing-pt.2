RED = True
BLACK = False


class Node:
    def __init__(
        self, value=None, priority=None, parent=None, left=None, right=None, color=RED
    ):
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent
        self.priority = priority


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        parent = None
        node = self.root

        while node is not None:
            parent = node
            if priority >= node.priority:
                node = node.left
            else:
                node = node.right

        if self.root is None:
            self.root = Node(value, priority, color=BLACK)
            self.insert_fixing(new_node)
            return

        if priority >= parent.priority:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.parent = parent

        self.insert_fixing(new_node)

    def left_rotate(self, node):
        x = node.right
        node.right = x.left

        if x.left is not None:
            x.left.parent = node
        x.parent = node.parent

        if node.parent is None:
            self.root = x
        elif node == node.parent.left:
            node.parent.left = x
        else:
            node.parent.right = x
        x.left = node
        node.parent = x

    def right_rotate(self, node):
        y = node.left
        node.left = y.right

        if y.right is not None:
            y.right.parent = node
        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    def insert_fixing(self, node):
        while node.parent and node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                node = self.handle_left_rotation(node)
            else:
                node = self.handle_right_rotation(node)

        self.root.color = BLACK

    def handle_left_rotation(self, node):
        while node != self.root and node.parent.color == RED:
            parent = node.parent
            if parent.parent.right and parent.parent.right.color == RED:
                parent.color = BLACK
                parent.parent.right.color = BLACK
                parent.parent.color = RED
                return parent.parent
            else:
                if node == parent.right:
                    node = parent
                    self.left_rotate(node)
                parent = node.parent
                parent.color = BLACK
                parent.parent.color = RED
                self.right_rotate(parent.parent)
                return node

    def handle_right_rotation(self, node):
        while node != self.root and node.parent.color == RED:
            parent = node.parent
            if parent.parent.left and parent.parent.left.color == RED:
                parent.parent.left.color = BLACK
                parent.color = BLACK
                parent.parent.color = RED
                return parent.parent
            else:
                if node == parent.left:
                    node = parent
                    self.right_rotate(node)
                parent = node.parent
                parent.color = BLACK
                parent.parent.color = RED
                self.left_rotate(parent.parent)
                return node

    def delete_max(self):
        if self.root is None:
            return None

        cur_node = self.root
        while cur_node.left:
            cur_node = cur_node.left

        node_to_be_deleted = cur_node

        if cur_node.parent:
            if node_to_be_deleted.parent.right == node_to_be_deleted:
                node_to_be_deleted.parent.right = None
            else:
                node_to_be_deleted.parent.left = None

            if node_to_be_deleted.right:
                self.transplant(node_to_be_deleted, node_to_be_deleted.right)
            else:
                self.transplant(node_to_be_deleted, node_to_be_deleted.left)
        else:
            self.root = None

        return node_to_be_deleted.value, node_to_be_deleted.priority

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v:
            v.parent = u.parent

    def balance_after_delete(self, node):
        while node != self.root and node.color == BLACK:
            if node == node.parent.left:
                node = self.balance_left(node)
            else:
                node = self.balance_right(node)
        node.color = BLACK

    def balance_left(self, node):
        sibling = node.parent.right
        if sibling.color == RED:
            sibling.color = BLACK
            node.parent.color = RED
            self.right_rotate(node.parent)
            sibling = node.parent.right
        if sibling.left.color == BLACK and sibling.right.color == BLACK:
            sibling.color = RED
            node = node.parent
        elif sibling.right.color == BLACK:
            sibling.left.color = BLACK
            sibling.color = RED
            self.left_rotate(sibling)
            sibling = node.parent.right
        else:
            sibling.color = node.parent.color
            node.parent.parent.color = BLACK
            sibling.right.color = BLACK
            self.right_rotate(node.parent)
            node = self.root
        return node

    def balance_right(self, node):
        sibling = node.parent.left
        if sibling.color == RED:
            sibling.color = BLACK
            sibling.parent.color = RED
            self.left_rotate(node.parent)
            sibling = node.parent.left
        if sibling.right.color == BLACK and sibling.left.color == BLACK:
            sibling.color = RED
            node = node.parent
        elif sibling.left.color == BLACK:
            sibling.right.color = BLACK
            sibling.color = RED
            self.right_rotate(sibling)
            sibling = node.parent.left
        else:
            sibling.color = node.parent.color
            node.parent.parent.color = BLACK
            sibling.left.color = BLACK
            self.left_rotate(node.parent)
            node = self.root
        return node

    def view_queue(self):
        if self.root is None:
            return []

        queue = []
        self._inorder_traversal(self.root, queue)
        return queue

    def _inorder_traversal(self, node, queue):
        if node is None:
            return
        self._inorder_traversal(node.left, queue)
        queue.append((node.value, node.priority))
        self._inorder_traversal(node.right, queue)
