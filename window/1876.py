def countGoodSubstrings(s: str) -> int:
    if len(s) < 3:
        return 0
    left = 0
    count = 0
    for right in range(3, len(s) + 1):
        string = s[left:right]
        if len(set(string)) == 3:
            count += 1
        left += 1
    return count


print(countGoodSubstrings(s = "abcd"))