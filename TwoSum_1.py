def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}
    for i, n in enumerate(nums):
        compliment = target - n
        if seen.get(compliment):
            return [seen[compliment], i]
        seen[n] = i
print(twoSum([2,7,11,15], 9))