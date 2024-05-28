"""
Merge Sort
- Divide and Conquer algorithm
- Recursive algorithm
- Two phases: Splitting and Merging
- Splitting phase leads to faster sorting during the merging phase
- Splitting is logical. We don't create new arrays.
"""


def merge(left, right):
    arr = []
    i, j = 0, 0
    left = left if left else []
    right = right if right else []

    while i + j < len(left) + len(right):
        left_val = left[i] if i < len(left) else float('inf')
        right_val = right[j] if j < len(right) else float('inf')

        if left_val < right_val:
            arr.append(left_val)
            i += 1
        else:
            arr.append(right_val)
            j += 1
    return arr


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    pivot = len(arr) // 2
    return merge(merge_sort(arr[:pivot]), merge_sort(arr[pivot:]))


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(merge_sort(arr))
