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


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, pivot_index, right):
    swap_index = pivot_index
    for i in range(pivot_index + 1, right + 1):
        if arr[i] < arr[pivot_index]:
            # swap with first bigger item than pivot
            swap_index += 1
            swap(arr, swap_index, i)
    # when loop is finished swap the pivot item with swap index
    swap(arr, pivot_index, swap_index)
    return swap_index


def quick_sort_inplace(arr, left, right):
    if left < right:
        swap_indx = partition(arr, left, right)
        quick_sort_inplace(arr, left, swap_indx - 1)
        quick_sort_inplace(arr, swap_indx + 1, right)
    return arr


if __name__ == "__main__":
    arr = [12, 4, 5, 6, 7, 3, 1, 15]
    print(quick_sort(arr))

    print(quick_sort_inplace(arr, 0, len(arr)-1))
