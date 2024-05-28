"""
Tree data structure
A tree is a data structure that consists of nodes in a parent/child relationship. It is a non-linear data structure.
It can contain as many children as needed. The top node is called the root node. The nodes at the bottom are called leaf nodes.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.data) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

    def __str__(self):
        return self.__repr__()


def build_tree():
    root = Node("Electronics")
    laptop = Node("Laptop")
    phone = Node("Phone")
    tv = Node("TV")
    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)
    return root


if __name__ == "__main__":
    tree = build_tree()
    print(tree)
    """
    Output:
    'Electronics'
        'Laptop'
        'Phone'
        'TV'
    """