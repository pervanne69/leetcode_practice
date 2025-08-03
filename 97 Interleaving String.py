# def isInterleave(s1: str, s2: str, s3: str) -> bool:
#     idx1, idx2 = 0, 0
#     for char in s3:
#
#         if idx1 < len(s1):
#             if s1[idx1] == char:
#                 idx1 += 1
#             else:
#                 if idx2 < len(s2):
#                     if s2[idx2] == char:
#                         idx2 += 1
#                     else:
#                         while (idx1 < len(s1) or idx2 < len(s2)) and (s1[idx1] != char and s2[idx2] != char):
#                             if idx1 < len(s1):
#                                 if s1[idx1] == char:
#                                     break
#                                 idx1 += 1
#                             elif idx2 < len(s2):
#                                 if s2[idx2] == char:
#                                     break
#                                 idx2 += 1
#                 else:
#                     while idx1 < len(s1) and s1[idx1] != char:
#                         idx1 += 1
#         else:
#             if idx2 < len(s2):
#                 if s2[idx2] == char:
#                     idx2 += 1
#                 else:
#                     while idx2 < len(s2) and s2[idx2] != char:
#                         idx2 += 1
#     return idx1 == len(s1) and idx2 == len(s2)
#
#
# print(isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))