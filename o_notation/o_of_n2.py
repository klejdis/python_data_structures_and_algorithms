"""
The O(n^2) notation is used to describe an algorithm that will execute in the same time
regardless of the size of the input data set. The time complexity of an algorithm is said
to be O(n^2) if the time taken by an algorithm to complete is proportional to the square
"""

import time


def print_pairs(data):
    for i in data:
        for j in data:
            # just smthg to do
            a = i + j


data = [1, 2, 3, 4, 5]

s_time = time.time()
print_pairs(data)
print("time for a few items:", time.time() - s_time)  # 0.0009999275207519531

data = [x for x in range(1000)]
s_time = time.time()
print_pairs(data)
print("for 1k", time.time() - s_time)  # 0.0009999275207519531

data = [x for x in range(10000)]
s_time = time.time()
print_pairs(data)
print("for 10k", time.time() - s_time)  # 0.0009999275207519531

data = [x for x in range(100000)]
s_time = time.time()
print_pairs(data)
print("for 100k", time.time() - s_time)  # very slow
