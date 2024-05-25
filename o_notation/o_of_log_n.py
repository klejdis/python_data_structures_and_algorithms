"""
The time complexity of an algorithm is said to be O(log n) if the time taken by the algorithm increases
logarithmically as the input size increases.
"""
import time


def o_of_log_n(n):
    i = 1
    while i < n:
        i = i * 2
    return i


s_time = time.time()
o_of_log_n(10)
print("Time taken for n=10: ", time.time() - s_time)

s_time = time.time()
o_of_log_n(100)
print("Time taken for n=100: ", time.time() - s_time)

s_time = time.time()
o_of_log_n(1000)
print("Time taken for n=1000: ", time.time() - s_time)

s_time = time.time()
o_of_log_n(10000)
print("Time taken for n=10000: ", time.time() - s_time)

s_time = time.time()
o_of_log_n(100000)
print("Time taken for n=100000: ", time.time() - s_time)

s_time = time.time()
o_of_log_n(1000000)
print("Time taken for n=1000000: ", time.time() - s_time)
