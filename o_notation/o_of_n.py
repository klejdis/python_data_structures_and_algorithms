"""
The O(n) notation is used to describe an algorithm whose performance will grow
linearly and in direct proportion to the size of the input data set.

"""


def find_max(data):
    max = data[0]
    for i in data:
        if i > max:
            max = i
    return max
