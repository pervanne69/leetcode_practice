from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    left = 0
    result = []
    n, m = len(s), len(p)
    right = 0
    d = {}
    while right < n:
        if s[right] in p and d.get(s[right], 0) <= p.count(s[right]) - 1:
            d[s[right]] = d.get(s[right], 0) + 1
            right += 1
            if right - left == m:
                result.append(left)
        else:
            if s[right] not in d:
                d = {}
                right += 1
                left = right
            else:
                while d.get(s[right]) != p.count(s[right]) - 1:
                    d[s[left]] -= 1
                    left += 1
    return result


print(findAnagrams(s = "baa", p = "aa"))
