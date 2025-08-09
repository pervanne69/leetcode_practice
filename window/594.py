# from collections import deque
# from typing import List
#
#
# def findLHS(nums: List[int]) -> int:
#     if len(nums) < 2:
#         return 0
#     left = 0
#     maxi = -10 ** 9
#     mini = 10 ** 10
#     cur_seq = deque()
#     cur_seq.append(nums[0])
#     max_length = 0
#     for right in range(1, len(nums)):
#         if nums[right] >= cur_seq[-1]:
#             cur_seq.append(nums[right])
#         elif nums[right] <= cur_seq[0]:
#             cur_seq.appendleft(nums[right])
#         maxi = cur_seq[-1]
#         mini = cur_seq[0]
#         if maxi - mini == 1:
#             max_length = max(max_length, right - left + 1)
#         else:
#             while maxi - mini != 1 and cur_seq and left < right:
#                 cur_seq.popleft()
#                 left += 1
#                 maxi = cur_seq[-1]
#                 mini = cur_seq[0]
#     return max_length
#
#
# print(findLHS(nums = [1,3,2,2,5,2,3,7]))
#
