"""
Exercises for the O-Notation chapter.

DONT FORGET TO DROP THE NON DOMINANT TERMS
"""


# Exercise 1
# ----------
def foo(array):
    sum = 0
    product = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    return sum, product


# answer: O(n)

# Exercise 2
# ----------
def print_pairs(array):
    for i in array:
        for j in array:
            print(i, j)


# answer: O(n^2)

# Exercise 3
# ----------
def print_unordered_pairs(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            print(array[i], array[j])


# How to calculate the time complexity of this function?
# The outer loop runs n times. The inner loop runs n - 1 times, then n - 2 times, and so on.
# The total number of iterations is n + (n - 1) + (n - 2) + ... + 1 = n(n + 1)/2
# Therefore, the time complexity is O(n^2)

# answer: O(n^2)


# Exercise 4
# ----------

def print_unordered_pairs_1(array_a, array_b):
    for i in range(len(array_a)):  # O(a)
        for j in range(len(array_b)):  # O(b)
            if array_a[i] < array_b[j]:  # O(1)
                print(array_a[i], array_b[j])  # O(1)


# answer: O(ab)

# Exercise 5
# ----------

def print_unordered_pairs_2(array_a, array_b):
    for i in range(len(array_a)):  # O(a)
        for j in range(len(array_b)):  # O(b)
            for k in range(0, 100000):  # O(b*100000)
                print(array_a[i], array_b[j])  # O(1)


# How to calculate the time complexity of this function?
# The outer loop runs a times. The first inner loop runs b times. The second inner loop runs 100000 times.
# answer: O(ab)


# Exercise 6
# ----------


def reverse(array):
    for i in range(len(array) // 2):  # O(n/2)
        other = len(array) - i - 1  # O(1)
        temp = array[i]  # O(1)
        array[i] = array[other]  # O(1)
        array[other] = temp  # O(1)


# How to calculate the time complexity of this function?
# The outer loop runs n/2 times. The time complexity is O(n/2) = O(n)
# answer: O(n)


# Exercise 7
# ----------

def intersection(array_a, array_b):
    for i in range(len(array_a)):  # O(a)
        for j in range(len(array_b)):  # O(b)
            if array_a[i] == array_b[j]:  # O(1)
                print(array_a[i], array_b[j])  # O(1)


# answer: O(ab)


# Exercise 8
# ----------

def intersection_1(array_a, array_b):
    array_a.sort()  # O(a log a)
    array_b.sort()  # O(b log b)
    i = 0  # O(1)
    j = 0  # O(1)
    while i < len(array_a) and j < len(array_b):  # O(a + b)
        if array_a[i] == array_b[j]:  # O(1)
            print(array_a[i], array_b[j])  # O(1)
            i += 1  # O(1)
            j += 1  # O(1)
        elif array_a[i] < array_b[j]:  # O(1)
            i += 1  # O(1)
        else:
            j += 1  # O(1)


# why does the sort has a time complexity of O(n log n)?
# The time complexity of the sort function is O(n log n) because it uses a comparison-based sorting algorithm.
# The most common comparison-based sorting algorithms are O(n^2) and O(n log n). The O(n^2) algorithms are
# bubble sort, insertion sort, and selection sort. The O(n log n) algorithms are merge sort, quicksort, and heapsort.
# answer: O(a log a + b log b)


# Exercise 9
# ----------
# example with O(nlogn) time complexity

def merge_sort(array):
    if len(array) <= 1:  # O(1)
        return array  # O(1)
    mid = len(array) // 2  # O(1)
    left = merge_sort(array[:mid])  # O(n/2 log(n/2))
    right = merge_sort(array[mid:])  # O(n/2 log(n/2))
    return list(merge(left, right))  # O(n)


# answer: O(nlog n)


def merge(left, right):
    result = []  # O(1)
    i = j = 0  # O(1)
    while i < len(left) and j < len(right):  # O(n)
        if left[i] < right[j]:  # O(1)
            result.append(left[i])  # O(1)
            i += 1  # O(1)
        else:
            result.append(right[j])  # O(1)
            j += 1  # O(1)
    result.extend(left[i:])  # O(n)
    result.extend(right[j:])  # O(n)
    return result  # O(1)


# Exercise 10
# ----------
# example with O(nlogn) time complexity

def quicksort(array):
    if len(array) <= 1:  # O(1)
        return array  # O(1)
    pivot = array[len(array) // 2]  # O(1)
    left = [x for x in array if x < pivot]  # O(n)
    middle = [x for x in array if x == pivot]  # O(n)
    right = [x for x in array if x > pivot]  # O(n)
    return quicksort(left) + middle + quicksort(right)  # O(n log n)


def count_ways(n):
    if n < 0:
        return 0

    # Initialize dp array
    dp = [0] * (n + 1)

    # Base case
    dp[0] = 1

    # Fill dp array using recurrence relation
    for i in range(1, n + 1):
        dp[i] += dp[i - 1] if i - 1 >= 0 else 0
        dp[i] += dp[i - 3] if i - 3 >= 0 else 0
        dp[i] += dp[i - 4] if i - 4 >= 0 else 0

    return dp[n]




# Example usage
n = 4
print(f"The number of ways to express {n} as a sum of 1, 3, and 4 is: {count_ways(n)}")
