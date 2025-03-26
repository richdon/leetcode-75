"""
ou are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


def largest_container_brute_force(heights: list[int]):
    n = len(heights)
    max_water = 0
    # find the maximum amount of water stored between all pairs of lines
    for i in range(n):
        for j in range(i + 1, n):
            height = min(heights[i], heights[j])
            width = j - i
            water = height * width
            max_water = max(water, max_water)
    print(max_water)
    return max_water


test_case1 = ([2, 7, 8, 3, 7, 6], 24)
test_case2 = ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)

# assert largest_container_brute_force(test_case1[0]) == test_case1[1]
# assert largest_container_brute_force(test_case2[0]) == test_case2[1]

def largest_container_two_pointer(heights: list[int]):
    n = len(heights)
    ptr_left = 0
    ptr_right = n-1
    max_water = 0

    while ptr_left < ptr_right:
        h = min(heights[ptr_left],  heights[ptr_right])
        w = ptr_right - ptr_left
        water = h * w
        max_water = max(water, max_water)
        if heights[ptr_left] < heights[ptr_right]:
            ptr_left += 1
        elif heights[ptr_left] > heights[ptr_right]:
            ptr_right -= 1
        else:
            ptr_right -= 1
            ptr_left += 1

    print(max_water)
    return max_water


test_case1 = ([2, 7, 8, 3, 7, 6], 24)
test_case2 = ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)

assert largest_container_two_pointer(test_case1[0]) == test_case1[1]
assert largest_container_two_pointer(test_case2[0]) == test_case2[1]