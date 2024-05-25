"""
Circular Linked List
- Circular linked list is a linked list where all nodes are connected to form a circle.
 There is no NULL at the end. A circular linked list can be a singly circular linked list or doubly circular linked
 list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        temp = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        self.head = new_node

    def remove(self, key):
        if self.head.data == key:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            if self.head == self.head.next:
                self.head = None
            else:
                self.head = self.head.next
                temp.next = self.head
        else:
            temp = self.head
            prev = None
            while temp.next != self.head:
                prev = temp
                temp = temp.next
                if temp.data == key:
                    prev.next = temp.next
                    temp = temp.next

    def __str__(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        return '->'.join(map(str, result))


if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.append(4)
    cll.append(5)
    print(cll)  # 1->2->3->4->5
    cll.prepend(0)
    print(cll)  # 0->1->2->3->4->5
    cll.remove(3)
    print(cll)  # 0->1->2->4->5
    cll.remove(0)
    print(cll)  # 1->2->4->5
    cll.remove(5)
    print(cll)  # 1->2->4
    cll.remove(4)
    print(cll)  # 1->2
    cll.remove(2)
    print(cll)  # 1
    cll.remove(1)
    print(cll)  # empty
    cll.remove(1)
    print(cll)  # empty
    cll.append(1)
    print(cll)  # 1
    cll.append(2)
    print(cll)  # 1->2
    cll.append(3)
    print(cll)  # 1->2->3
    cll.append(4)
    print(cll)  # 1->2->3->4
    cll.append(5)
    print(cll)  # 1->2->3->4->5
    cll.remove(1)
    print(cll)  # 2->3->4->5
    cll.remove(5)
    print(cll)  # 2->3->4
    cll.remove(4)
    print(cll)  # 2->3
    cll.remove(3)
    print(cll)  # 2
    cll.remove(2)
    print(cll)  # empty
    cll.remove(2)
    print(cll)  # empty
    cll.append(1)
    print(cll)  # 1
    cll.append(2)
    print(cll)  # 1->2
    cll.append(3)
    print(cll)  # 1->2->3
