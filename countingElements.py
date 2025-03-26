def countingElements(arr):
    sett = set()
    ans = 0
    for num in arr:
        sett.add(num + 1)
    for num in arr:
        if num in sett:
            ans += 1
    return ans

e = countingElements([1,3,2,3,5,0])

