def characterReplacement(s: str, k: int):
    count = {}
    max_freq = 0
    left = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]
        count[char] = count.get(char, 0) + 1
        max_freq = max(max_freq, count[char])
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)

    return max_length




# print(characterReplacement(s = "ABAB", k = 2))
print(characterReplacement("AABABBA", 1))  # → 4