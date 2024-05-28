"""
Selection Sort
- Time complexity: O(n^2)
- Space complexity: O(1)
- Unstable

1. Find the smallest element in the array and swap it with the first element.
2. Find the second-smallest element in the array and swap it with the second element.
3. Continue this process until the entire array is sorted.
"""


def selection_sort(data):
    for i in range(len(data)):
        min = i
        for j in range(i, len(data)):
            if data[min] > data[j]:
                min = j
        # swap
        data[i], data[min] = data[min], data[i]


if __name__ == "__main__":
    data = [3, 4, 2, 1, 5]
    selection_sort(data)
    print(data)
