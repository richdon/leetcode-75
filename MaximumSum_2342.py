from collections import defaultdict


def maximumSum(nums: list[int]):
    def get_digit_sum(num):
        digit_sum = 0
        while num:
            digit_sum += num % 10
            num //= 10

        return digit_sum

    dictt = defaultdict(list)
    for num in nums:
        key = get_digit_sum(num)
        dictt[key].append(num)
    ans = -1
    for nums in dictt.values():
        if len(nums) > 1:
            nums.sort(reverse=True)
            ans = max(ans, sum(nums[:2]))
    return ans

print(maximumSum([368,369,307,304,384,138,90,279,35,396,114,328,251,364,300,191,438,467,183]))