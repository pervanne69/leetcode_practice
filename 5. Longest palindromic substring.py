def longestPalindrome(s: str) -> str:
    if not s:
        return ""

    end = start = 0

    for i in range(len(s)):
        even_substring = expand_around_center(s, i, i + 1)
        odd_substring = expand_around_center(s, i, i)
        max_len = max(even_substring, odd_substring)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    return s[start:end + 1]


def expand_around_center(string: str, left: int, right: int) -> int:
    n = len(string)
    while left >= 0 and right <= n - 1 and string[left] == string[right]:
        left -= 1
        right += 1
    return right - left - 1
