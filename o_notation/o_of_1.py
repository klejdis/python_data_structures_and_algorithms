"""
The O(1) notation is used to describe an algorithm that will always execute in the
same time (or space) regardless of the size of the input data set.
"""
import time

from isort.sorting import sort


def o_of_1(data, index):
    return data[index]


data = [1, 2, 3, 4, 5]
s_time = time.time()


o_of_1(data, 0)
print(time.time() - s_time)  # 0.00000023841857910156

o_of_1(data, 4)
print(time.time() - s_time)  # 0.00000023841857910156

# identical time to execute the function, regardless of the size of the input data set
