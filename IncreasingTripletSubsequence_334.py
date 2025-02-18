def increasing_triplet_subsequence(nums: list[int]):
    i = j = float("inf")
    for num in nums:
        if num <= i:
            i = num
        elif num <= j:
            j = num
        else:
            return True
    return False


assert increasing_triplet_subsequence([20,100,10,12,5,13]) == True
assert increasing_triplet_subsequence([1, 2, 3, 4, 5]) == True
assert increasing_triplet_subsequence([5, 4, 3, 2, 1]) == False
assert increasing_triplet_subsequence([2, 1, 5, 0, 4, 6]) == True