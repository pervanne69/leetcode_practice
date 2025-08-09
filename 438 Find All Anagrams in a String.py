from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    return sol2(s, p)


def sol1(s: str, p: str) -> List[int]:
    n, m = len(s), len(p)
    if m > n:
        return []
    target = {}
    for char in p:
        target[char] = target.get(char, 0) + 1

    left = 0
    result = []
    window = {}
    for right in range(n):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        while right - left + 1 > m:
            left_char = s[left]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            left += 1

        if right - left + 1 == m and window == target:
            result.append(left)

    return result

def sol2(s: str, p: str) -> List[int]:
    if len(p) > len(s):
        return []

    result = []
    count_p = [0] * 26
    count_s = [0] * 26

    for ch in p:
        count_p[ord(ch) - ord('a')] += 1

    for i in range(len(s)):
        count_s[ord(s[i]) - ord('a')] += 1

        if i >= len(p):
            # Удаляем символ, выходящий из окна
            count_s[ord(s[i - len(p)]) - ord('a')] -= 1

        if count_s == count_p:
            result.append(i - len(p) + 1)

    return result





print(findAnagrams(s = "cbaebabacd", p = "abc"))
