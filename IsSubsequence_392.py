def is_subsequence(s, t):
    for char in t:
        if s[0] == char:
            s.pop(0)
        if s == "":
            return True
    return False

is_subsequence("abc", "ahbgdc")