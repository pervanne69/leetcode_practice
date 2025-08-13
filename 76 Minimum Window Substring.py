from collections import deque


def minWindow(s: str, t: str) -> str:
    t_freq = dict()
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1
    left = 0
    cur_left = 0
    cur_right = 0
    cur_freq = dict()
    min_length = 10 ** 5 + 7
    need = len(t_freq)
    have = 0
    for right in range(len(s)):
        if s[right] in t_freq:
            cur_freq[s[right]] = cur_freq.get(s[right], 0) + 1
            if cur_freq[s[right]] == t_freq[s[right]]:
                have += 1
        while left <= right and have == need:
            if min_length > right - left + 1:
                min_length = right - left + 1
                cur_left = left
                cur_right = right + 1
            if s[left] in t_freq:
                if cur_freq[s[left]] == t_freq[s[left]]:
                    have -= 1
                cur_freq[s[left]] -= 1
                if cur_freq[s[left]] == 0:
                    del cur_freq[s[left]]
            left += 1
    return s[cur_left:cur_right]


print(minWindow(s="ADOBECODEBANC", t = "ABC"))