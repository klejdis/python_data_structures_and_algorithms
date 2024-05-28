"""
Heap Sort
- Time complexity: O(nlogn)
- Space complexity: O(1)
- Not stable
- Not adaptive
- In-place
- Comparison sort
- Heapsort is an in-place algorithm, but it is not a stable sort.
"""


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    # Test
    arr = [2, 7, 5, 11, 12, 13, 6]
    print(heap_sort(arr))  # [5, 6, 7, 11, 12, 13]
