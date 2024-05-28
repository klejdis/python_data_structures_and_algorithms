"""
Quick Sort Algorithm
it is a divide and conquer algorithm
it works by selecting a 'pivot' element from the array and partitioning the other elements into
two sub-arrays according to whether they are less than or greater than the pivot
The sub-arrays are then sorted recursively

Time Complexity:
    Best Case: O(n log n)
    Average Case: O(n log n)
    Worst Case: O(n^2)
"""


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = len(arr) // 2
    less = []
    equal = []
    bigger = []
    for i in arr:
        if i < arr[pivot]:
            less.append(i)
        elif i == arr[pivot]:
            equal.append(i)
        else:
            bigger.append(i)
    return quick_sort(less) + equal + quick_sort(bigger)


if __name__ == "__main__":
    arr = [12, 4, 5, 6, 7, 3, 1, 15]
    print(quick_sort(arr))
