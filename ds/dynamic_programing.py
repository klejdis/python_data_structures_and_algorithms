"""
Dynamic Programming
- A method for solving a complex problem by breaking it down into a collection of simpler subproblems,
solving each of those subproblems just once, and storing their solutions.
"""


# 1. Fibonacci Series
# -------------------
# The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones,
# usually starting with 0 and 1.
#
# The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
#
# The nth number in the sequence is called the nth Fibonacci number.

# Recursive Solution
# ------------------
# Time Complexity: O(2^n)
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Dynamic Programming Solution
# ----------------------------
# Time Complexity: O(n)
def fibonacci_dynamic(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


# 2. Longest Common Subsequence
# -----------------------------
# Given two sequences, find the length of the longest subsequence present in both of them.
# A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
#
# For example, "abc", "abg", "bdf", "aeg", "acefg", .. etc are subsequences of "abcdefg".
# So a string of length n has 2^n different possible subsequences.

# Dynamic Programming Solution

# Time Complexity: O(m*n)

def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


print(longest_common_subsequence("abcde", "ace"))


# 3. House Robber
# ---------------
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected,
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#

# Dynamic Programming Solution
# Time Complexity: O(n)

def house_robber(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    return max(rob(nums[:-1]), rob(nums[1:]))


def rob(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    dp[1] = nums[0]
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
    return dp[n]


print(house_robber([2, 3, 2, 5]))  # 3
