"""
The o(n!) notation is used to describe an algorithm whose growth doubles with each addition to the input data set.
"""


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)



