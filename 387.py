def firstUniqChar(s: str) -> int:
    return sol1(s)


def sol1(s: str) -> int:
    d = {}
    mini = 10 ** 10
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = [i]
        else:
            d[s[i]].append(i)
    for indexes in d.values():
        if len(indexes) == 1:
            mini = min(indexes[0], mini)
    return mini if mini < 10 ** 10 else -1


print(firstUniqChar("aabb"))
