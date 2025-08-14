# 340. Longest Substring with At Most K Distinct Characters
# Given a strings and an integer k,
# return the length of the longest substring of s that contains at most k distinct characters.

# Example 1:
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.

# Example 2:
# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.

# Constraints:
# • 1 <= s. length <= 5 * 104
# • 8く=kく=50

def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    seen = dict()
    left = 0
    maxi = 0
    for right in range(len(s)):
        seen[s[right]] = seen.get(s[right], 0) + 1
        while left <= right and len(seen) > k:
            if s[left] in seen:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
            left += 1
        maxi = max(maxi, right - left + 1)
    return maxi

print(lengthOfLongestSubstringKDistinct(s = "aa", k = 1))