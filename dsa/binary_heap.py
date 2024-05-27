"""
Binary Heap
- A binary heap is a complete binary tree which satisfies the heap ordering property.
- The heap ordering property is as follows:
    - In a max binary heap, the key at root must be greater than or equal to the keys at its children.
    - In a MIN binary heap, the key at root must be less than or equal to the keys at its children.
"""


class BinaryMinHeap:
    def __init__(self, size):
        self.heap = [None] * (size + 1)
        self.heap_size = 0
        self.max_size = size + 1

    def parent(self, i):
        return i // 2

    def left_child(self, i):
        return 2 * i

    def right_child(self, i):
        return 2 * i + 1

    def insert(self, value, heap_type='MIN'):
        if self.heap_size + 1 == self.max_size:
            return "Heap is full"
        self.heap[self.heap_size + 1] = value
        self.heap_size += 1
        self.heapify_tree_on_insert(self.heap_size, heap_type)

    def heapify_tree_on_insert(self, index, heap_type):
        parent = self.parent(index)
        if index <= 1:
            return

        if heap_type == "MIN":
            if self.heap[parent] > self.heap[index]:
                # swap
                tmp = self.heap[parent]
                self.heap[parent], self.heap[index] = self.heap[index], tmp
                self.heapify_tree_on_insert(parent, heap_type)
        if heap_type == "MAX":
            if self.heap[parent] < self.heap[index]:
                # swap
                tmp = self.heap[parent]
                self.heap[parent], self.heap[index] = self.heap[index], tmp
                self.heapify_tree_on_insert(parent, heap_type)

    def extract(self, heap_type="MIN"):
        if self.heap_size == 0:
            return
        extract_value = self.heap[1]
        self.heap[1] = self.heap[self.heap_size]
        self.heap[self.heap_size] = None

        self.heapify_tree_on_extract(1, heap_type)

        return extract_value

    def heapify_tree_on_extract(self, index, heap_type):
        left_child = self.left_child(index)
        right_child = self.right_child(index)

        # stop condition
        if self.heap_size < left_child:
            return

        # only 1 child
        if self.heap_size == left_child:
            # only one left child, check and return
            if heap_type == "MIN":
                if self.heap[index] > self.heap[left_child]:
                    self.swap_indexes_values(index, left_child)
            if heap_type == "MAX":
                if self.heap[index] < self.heap[left_child]:
                    self.swap_indexes_values(index, left_child)
            return

        # has 2 children,
        if heap_type == "MIN":
            # the child who is the smallest has to pop up in case of MIN heap
            if self.heap[right_child] is None or self.heap[left_child] < self.heap[right_child]:
                if self.heap[index] > self.heap[left_child]:
                    self.swap_indexes_values(index, left_child)
                    self.heapify_tree_on_extract(left_child, heap_type)
            else:
                # the child whi is the greatest has to pop up in case of MAX heap
                if self.heap[index] > self.heap[right_child]:
                    self.swap_indexes_values(index, right_child)
                    self.heapify_tree_on_extract(right_child, heap_type)
            return

        if heap_type == "MAX":
            # the child who is the greatest has to pop up in case of MAX heap
            if self.heap[right_child] is None or self.heap[left_child] > self.heap[right_child]:
                if self.heap[index] < self.heap[left_child]:
                    self.swap_indexes_values(index, left_child)
                    self.heapify_tree_on_extract(left_child, heap_type)
            else:
                # the child whi is the greatest has to pop up in case of MAX heap
                if self.heap[index] < self.heap[right_child]:
                    self.swap_indexes_values(index, right_child)
                    self.heapify_tree_on_extract(right_child, heap_type)
            return

    def swap_indexes_values(self, index, index_2):
        tmp = self.heap[index]
        self.heap[index], self.heap[index_2] = self.heap[index_2], tmp


if __name__ == "__main__":
    heap = BinaryMinHeap(6)
    heap.insert(4, "MIN")
    heap.insert(3, "MIN")
    heap.insert(2, "MIN")
    heap.insert(1, "MIN")
    heap.insert(-1, "MIN")
    heap.extract("MIN")

    print(heap.heap)

    heap = BinaryMinHeap(6)
    heap.insert(3, "MAX")
    heap.insert(4, "MAX")
    heap.insert(2, "MAX")
    heap.insert(1, "MAX")
    print(heap.heap)

    import heapq

    heap = []
    heapq.heappush(heap, 4)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 2)
    heapq.heappush(heap, 1)

    print(heapq.nlargest(2, heap))
    print(heapq.nsmallest(2, heap))

    print(heap)
