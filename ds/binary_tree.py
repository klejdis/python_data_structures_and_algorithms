"""
Binary Tree
- A tree whose elements have at most 2 children is called a binary tree.
- Since each element in a binary tree can have only 2 children, we typically name them the left and right child.
- A Binary Tree node contains following parts.
    - Data
    - Pointer to left child
    - Pointer to right child
- A Binary Tree can be traversed in two ways:
    - Depth First Traversal: Inorder, Preorder, Postorder
    - Breadth First Traversal: Level Order Traversal
"""


# Binary Tree Representation in Python

# list representation

class BinaryTree:
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size

    def insert_node(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "The Binary Tree is full"
        self.custom_list[self.last_used_index + 1] = value
        self.last_used_index += 1
        return "The value has been successfully inserted"

    def search_node(self, node_value):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == node_value:
                return "Success"
        return "Not found"

    def preorder_traversal(self, index):
        if index > self.last_used_index:
            return
        print(self.custom_list[index])
        self.preorder_traversal(index * 2)
        self.preorder_traversal(index * 2 + 1)

    def inorder_traversal(self, index):
        if index > self.last_used_index:
            return
        self.inorder_traversal(index * 2)
        print(self.custom_list[index])
        self.inorder_traversal(index * 2 + 1)

    def postorder_traversal(self, index):
        if index > self.last_used_index:
            return
        self.postorder_traversal(index * 2)
        self.postorder_traversal(index * 2 + 1)
        print(self.custom_list[index])

    def level_order_traversal(self, index):
        for i in range(index, self.last_used_index + 1):
            print(self.custom_list[i])

    def delete_node(self, value):
        if self.last_used_index == 0:
            return "There is not any node to delete"
        for i in range(1, self.last_used_index + 1):
            if self.custom_list[i] == value:
                self.custom_list[i] = self.custom_list[self.last_used_index]
                self.custom_list[self.last_used_index] = None
                self.last_used_index -= 1
                return "The node has been successfully deleted"
        return "The value does not exist in the Binary Tree"


# Using linked list


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTreeLL:
    def __init__(self, root=None):
        self.root = Node(root) if root is not None else None

    def insert_node(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_node(value, self.root)

    def _insert_node(self, value, current_node):
        # insert with level order traversal
        queue = [current_node]
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.left is None:
                current_node.left = Node(value)
                break
            else:
                queue.append(current_node.left)
            if current_node.right is None:
                current_node.right = Node(value)
                break
            else:
                queue.append(current_node.right)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, current_node):
        # search with level order traversal
        if current_node is None:
            return False
        queue = [current_node]
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.value == value:
                return True
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + " ")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + " ")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + " ")
        return traversal

    def level_order_traversal(self, start):
        if start is None:
            return
        queue = [start]
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue[0].value) + " "
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return traversal

    def get_deepest_node(self):
        if self.root is None:
            return
        queue = [self.root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return node.value  # last node in the queue

    def delete_deepest_node(self, d_node):
        if self.root is None:
            return
        queue = [self.root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node is d_node:
                node = None
                return
            if node.right:
                if node.right is d_node:
                    node.right = None
                    return
                else:
                    queue.append(node.right)
            if node.left:
                if node.left is d_node:
                    node.left = None
                    return
                else:
                    queue.append(node.left)

    def delete_node(self, value):
        if self.root is None:
            return "The binary tree is empty"
        if self.root.left is None and self.root.right is None:
            if self.root.value == value:
                self.root = None
                return "The root node has been successfully deleted"
            else:
                return "The value does not exist in the binary tree"
        queue = [self.root]
        d_node = None
        while len(queue) > 0:
            node = queue.pop(0)
            if node.value == value:
                d_node = node
                break
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if d_node:
            x = self.get_deepest_node()
            d_node.value = x
            self.delete_deepest_node(x)
            return "The node has been successfully deleted"
        return "The value does not exist in the binary tree"

    def __str__(self):
        # str representation of the binary tree printed on console with hierarchy
        return self.print_tree(self.root)

    def print_tree(self, root, level=0, prefix="Root: "):
        # If the tree is empty, return an empty string
        if root is None:
            return ""

        # Create the string representation for the current node
        result = " " * (level * 4) + prefix + str(root.value) + "\n"

        # Recursively create the string representation for the left and right subtrees
        if root.left is not None or root.right is not None:
            if root.left:
                result += self.print_tree(root.left, level + 1, "L--- ")
            else:
                result += " " * ((level + 1) * 4) + "L--- None\n"
            if root.right:
                result += self.print_tree(root.right, level + 1, "R--- ")
            else:
                result += " " * ((level + 1) * 4) + "R--- None\n"

        return result


if __name__ == "__main__":
    bt = BinaryTreeLL(5)
    bt.insert_node(3)
    bt.insert_node(7)
    bt.insert_node(1)
    bt.insert_node(4)
    bt.insert_node(6)
    print(bt)
    print(bt.preorder_traversal(bt.root, ""))
    print(bt.inorder_traversal(bt.root, ""))
    print(bt.postorder_traversal(bt.root, ""))
