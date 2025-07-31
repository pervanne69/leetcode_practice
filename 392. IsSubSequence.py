def isSubSequence(s: str, t: str) -> bool:
    s = sorted(s)
    t = sorted(set(t))
    k = count = 0
    while k < len(s) and k < len(t):
        if s[k] == t[k]:
            count += 1
        k += 1
    return count == len(s)


print(isSubSequence( s = "abc", t = "ahbgdc"))

