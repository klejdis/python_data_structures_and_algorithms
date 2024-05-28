"""
Bucket Sort
- Distribute the elements of an array into a number of buckets
- Each bucket is then sorted individually, either using a different sorting algorithm,
 or by recursively applying the bucket sorting algorithm
- Bucket sort is mainly useful when input is uniformly distributed over a range
"""
import math
from insertion_sort import insertion_sort


def bucket_sort(arr):
    num_of_buckets = round(math.sqrt(len(arr)))
    buckets = []
    max_val = max(arr)

    for i in range(num_of_buckets):
        buckets.append([])

    for j in arr:
        bucket_of_element = math.ceil(j * num_of_buckets / max_val)
        buckets[bucket_of_element-1].append(j)

    for k in range(num_of_buckets):
        buckets[k] = insertion_sort(buckets[k])

    k = 0
    for i in range(num_of_buckets):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1
    return arr


if __name__ == '__main__':
    arr = [2, 3, 4, 5]
    print(bucket_sort(arr))
