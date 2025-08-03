# def longestSubstring(s: str, k: int) -> int:
#     max_len = 0
#
#     max_unique = []
#     for i in s:
#         if i not in max_unique:
#             max_unique.append(i)
#
#     for target_unique in range(1, len(max_unique) + 1):
#         count = [0] * 26
#         left = right = 0
#         unique = 0
#         at_least_k = 0
#
#         while right < len(s):
#             if unique <= target_unique:
#                 idx = ord(s[right]) - ord('a')
#                 if count[idx] == 0:
#                     unique += 1
#                 count[idx] += 1
#                 if count[idx] == k:
#                     at_least_k += 1
#                 right += 1
#             else:
#                 idx = ord(s[left]) - ord('a')
#                 if count[idx] == k:
#                     at_least_k -= 1
#                 count[idx] -= 1
#                 if count[idx] == 0:
#                     unique -= 1
#                 left += 1
#
#             if unique == at_least_k == target_unique:
#                 max_len = max(max_len, right - left)
#
#     return max_len
#



def longestSubstring(s: str, k: int) -> int:
    max_length = 0

    max_unique = []
    for i in s:
        if i not in max_unique:
            max_unique.append(i)

    for target_unique in range(1, len(max_unique) + 1):
        count = [0] * len(max_unique)
        unique = 0
        at_least_k = 0
        left = right = 0

        while right < len(s):
            if unique <= target_unique:
                idx = ord(s[right]) - ord("a")
                if count[idx] == 0:
                    unique += 1
                count[idx] += 1
                if count[idx] == k:
                    at_least_k += 1
                right += 1
            else:
                idx = ord(s[left]) - ord("a")
                if count[idx] == k:
                    at_least_k -= 1
                count[idx] -= 1
                if count[idx] == 0:
                    unique -= 1
                left += 1

            if unique == at_least_k == target_unique:
                max_length = max(max_length, right - left)
    return max_length

print(longestSubstring("bbaaacbd", k = 3))