# Exercise: 1
# find the nth element from last in a singly linked list

# Time complexity: O(n)
# Space complexity: O(1)

from linked_list import LinkedList


def find_nth_from_last(ll, n):
    if ll.head is None:
        return None

    current = ll.head
    nth = ll.head

    for i in range(n):
        if nth is None:
            return None
        nth = nth.next

    while nth:
        current = current.next
        nth = nth.next

    return current


# Exercise: 2
# sort around a given value so that all nodes less than the value come before all nodes greater than or equal to the
# value come after. The original order of the nodes should be preserved.

# Time complexity: O(n)

def sort_around_value(ll, value):
    if ll.head is None:
        return None

    current = ll.head
    less_than = LinkedList()
    greater_than = LinkedList()

    while current:
        if current.data < value:
            less_than.append(current.data)
        else:
            greater_than.append(current.data)
        current = current.next

    current = less_than.head
    while current.next:
        current = current.next

    current.next = greater_than.head

    return less_than


# Exercise: 3
# remove duplicates from an unsorted linked list

# Time complexity: O(n)
# Space complexity: O(n)

def remove_duplicates(ll):
    if ll.head is None:
        return None

    current = ll.head
    seen = {current.data}
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next

    return ll


def longest_subseq_with_diff_one(a, n):
    # DP array initialized to 1, as the smallest subsequence length is 1
    dp = [1] * n

    # Build the DP array
    for i in range(1, n):
        for j in range(i):
            if abs(a[i] - a[j]) == 1:
                dp[i] = max(dp[i], dp[j] + 1)

    # The length of the longest subsequence
    return max(dp)


# Example input
n = 7
a = [10, 9, 4, 5, 4, 8, 6]

# Output the result
print(longest_subseq_with_diff_one(a, n))  # Output: 3
