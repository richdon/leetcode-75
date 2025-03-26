from collections import defaultdict


def equalPairs(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    rows = defaultdict(int)
    cols = defaultdict(int)

    for i, row in enumerate(grid):
        rows[tuple(row)] += 1
        col = []
        for j in range(len(row)):
            col.append(grid[j][i])
        cols[tuple(col)] += 1

    ans = 0
    for key, value in rows.items():
        ans = max(ans, value * cols[key])
    return ans

