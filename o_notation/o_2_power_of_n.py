"""
The time complexity of the following code is O(2^n) because the function is called twice recursively.
"""


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(5))  # 0, 1, 1, 2, 3, 5
    print(fibonacci(10))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    print(fibonacci(6))  # 0, 1, 1, 2, 3, 5, 8
