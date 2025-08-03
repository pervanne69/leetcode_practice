# def numDecodings(self, s: str) -> int:
#     mapping = {str(i): chr(ord('A') + i - 1) for i in range(1, 27)}
#     count = 0
#     left = 0
#     for right in range(len(s)):
#         if s[right] in mapping:
#             count += 1
#         else:
#             while s[left]



# For example, "11106" can be decoded into:
#
# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).