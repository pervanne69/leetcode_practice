# 159. Longest Substring with At Most Two Distinct Characters
# Given a string s, return the length of the longest substring that contains at most
# two distinct characters.
# Example 1:
# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.

# Example 2:
# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.

# Constraints:
# • 1 <= s. length <= 105
# • s consists of English letters.

def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    seen = dict()
    left = 0
    maxi = 0
    for right in range(len(s)):
        seen[s[right]] = seen.get(s[right], 0) + 1
        while left <= right and len(seen) > 2:
            if s[left] in seen:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
            left += 1
        maxi = max(maxi, right - left + 1)
    return maxi


print(lengthOfLongestSubstringTwoDistinct("ccaabbb"))