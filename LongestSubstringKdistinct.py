from collections import defaultdict
def find_longest_substring(string, k):
    counts = defaultdict(int)
    left = ans = 0
    for right, char in enumerate(string):
        counts[char] += 1
        while len(counts) > k:
            c = string[left]
            counts[c] -= 1
            if counts[c] == 0:
                del counts[c]
            left += 1
        ans = max(ans, right - left + 1)
    return ans

print(find_longest_substring("eceba", 2))