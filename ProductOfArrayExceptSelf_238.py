"""
- create an empty array
- start window = 0
- iterate
"""


def product_except_self(nums: list[int]):
    res = [1] * len(nums)
    prefix = 1
    for idx, _ in enumerate(nums):
        res[idx] = prefix
        prefix *= nums[idx]

    postfix = 1
    for idx in range(len(nums) - 1, -1, -1):
        res[idx] *= postfix
        postfix *= nums[idx]
    return res


if __name__ == '__main__':
    actual = product_except_self([1, 2, 3, 4])
    assert actual == [24, 12, 8, 6]
