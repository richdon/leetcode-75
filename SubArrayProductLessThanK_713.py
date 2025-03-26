def numSubarrayProductLessThanK(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """



r = numSubarrayProductLessThanK([10,5,2,6], 100)
r = numSubarrayProductLessThanK([10,9,10,4,3,8,3,3,6,2,10,10,9,3], 19)
print(r)
assert r == 18