def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans = []
    for i, x in enumerate(nums):
        seen = set()
        for j, y in enumerate(nums[i+1:], i+1):
            z = 0 - x - y
            if z in seen:
                a = sorted([x, y, z])
                if a not in ans:
                    ans.append(a)
            else:
                seen.add(y)
    return ans

#print(threeSum([-1,0,1,2,-1,-4]))