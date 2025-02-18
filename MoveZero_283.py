def move_zeros(nums: list[int]):
    nums_length = len(nums) - 1

    for i in range(nums_length, -1, -1):
        if nums[i] == 0:
            last_pos = i
            while last_pos < nums_length:
                temp = nums[last_pos + 1]
                nums[last_pos + 1] = nums[last_pos]
                nums[last_pos] = temp
                last_pos += 1



#move_zeros([1,0])


def move_zeros(nums):
    pos = 0

    for i in range(len(nums)):
        el = nums[i]
        if el != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

move_zeros([0,1,0,3,12])
