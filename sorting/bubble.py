"""
Bubble Sort Algorithm
it is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order.
"""


def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


if __name__ == '__main__':
    data = [5, 2, 9, 1, 5, 6]
    bubble_sort(data)
    print(data)
