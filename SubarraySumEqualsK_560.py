"""
Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.
"""

from collections import defaultdict
def subarray_sum_equals_k(nums, k):
    counts = {}
    counts[0] = 1

    curr = ans = 0

    for num in nums:
        curr += num
        compliment = curr - k
        ans += counts.get(compliment, 0)
        if counts.get(curr):
            counts[curr] += 1
        else:
            counts[curr] = 1
    return ans

print(subarray_sum_equals_k([1, 2, 1, 2, 1], 3))