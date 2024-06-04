"""
Linear search algorithm
is a simple search algorithm that searches for a target value within a list.
It sequentially checks each element of the list for the target value until a match is found or until all the elements
have been searched.

Time complexity: O(n)
"""


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Example
arr = [2, 3, 4, 10, 40]
target = 10
result = linear_search(arr, target)
if result != -1:
    print(f"Element is present at index {result}")
