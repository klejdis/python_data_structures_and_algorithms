"""
Binary search algorithm
is a search algorithm that finds the position of a target value within a sorted array.
Binary search compares the target value to the middle element of the array.
If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the
remaining half,

Binary search runs in logarithmic time in the worst case, making O(log n) comparisons, where n is the number of
elements in the array.
"""


def binary_search(arr, target):
    """
    Binary search algorithm
    :param arr: list of elements
    :param target: element to search
    :return: index of target element
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    print(binary_search(arr, target))  # Output: 4
    target = 10
    print(binary_search(arr, target))  # Output: -1