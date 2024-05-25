"""
The time complexity of the following code is O(2^n) because the function is called twice recursively.
"""


def fibonacci(n):
    if n <= 1:  # O(1)
        return n  # O(1)
    return fibonacci(n - 1) + fibonacci(n - 2)  # O(2^n)
