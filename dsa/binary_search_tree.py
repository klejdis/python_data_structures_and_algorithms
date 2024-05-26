"""
Binary Search Tree
- A binary search tree is a binary tree in which every node
fits a specific ordering property: all left descendents <= n < all right descendents.
"""

import binary_tree as bt


class BinarySearchTree(bt.BinaryTreeLL):
    def __init__(self, root=None):
        super().__init__(root)

    def insert_node(self, value):
        if self.root is None:
            self.root = bt.Node(value)
        else:
            self._insert_node(value, self.root)

    def _insert_node(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = bt.Node(value)
            else:
                self._insert_node(value, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = bt.Node(value)
            else:
                self._insert_node(value, current_node.right)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, current_node):
        if current_node is None:
            return "The value does not exist in the Binary Search Tree"
        if value == current_node.value:
            return "Success"
        if value < current_node.value:
            return self._search(value, current_node.left)
        else:
            return self._search(value, current_node.right)

    def delete_node(self, value):
        if self.root is None:
            return "The binary tree is empty"
        else:
            return self._delete_node(value, self.root)

    def _delete_node(self, value, current_node):
        if value < current_node.value:
            current_node.left = self._delete_node(value, current_node.left)
        elif value > current_node.value:
            current_node.right = self._delete_node(value, current_node.right)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            # if is leaf node just delete it
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            else:
                # if the node has two children, replace the value of the node with the smallest value of the right subtree
                current_node.value = self._min_value(current_node.right)
                current_node.right = self._delete_node(current_node.value, current_node.right)
        return current_node

    def _min_value(self, current_node):
        min_value = current_node.value
        while current_node.left:
            min_value = current_node.left.value
            current_node = current_node.left
        return min_value


# example
bst = BinarySearchTree()
bst.insert_node(70)
bst.insert_node(50)
bst.insert_node(90)
bst.insert_node(30)
bst.insert_node(60)
bst.insert_node(80)
bst.insert_node(100)
bst.insert_node(20)
bst.insert_node(40)


print(bst.print_tree(bst.root))
print(bst.delete_node(70))  # Success
print(bst.print_tree(bst.root))
