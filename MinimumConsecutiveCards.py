"""
You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.
"""
from collections import defaultdict


def minimumCardPickup(cards):
    """
    :type cards: List[int]
    :rtype: int
    """
    idx = defaultdict(list)
    ans = float("inf")

    for i, num in enumerate(cards):
        idx[num].append(i)

    for indexes in idx.values():
        for i, index in enumerate(indexes[:-1]):
            ans = min(ans, indexes[i+1] - index + 1)
    return ans

print(minimumCardPickup([3,4,2,3,4,7]))