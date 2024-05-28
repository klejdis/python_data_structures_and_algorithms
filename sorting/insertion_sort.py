"""
Insertion Sort
- Time complexity: O(n^2)
- Space complexity: O(1)
- Stable
- In-place

1. Start from the second element, compare it with the first element
2. If the second element is smaller, swap them
3. Move to the third element, compare it with the second element
4. If the third element is smaller, swap them
5. Repeat until the last element

"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    arr = [1, 3, 3, 5, 4]
    print(insertion_sort(arr))
    # Output: [1, 2, 3, 4, 5]
