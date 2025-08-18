from typing import List
from collections import deque


# def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
#     result = deque()
#     n = len(arr)
#     median_index = get_median_index(arr, x)
#     if median_index == 0:
#         for i in range(k):
#             result.append(arr[i])
#     elif median_index == len(arr) - 1:
#         for i in range(n - 1, n - k - 1, -1):
#             result.appendleft(arr[i])
#     else:
#         result.append(arr[median_index])
#         right_idx, left_idx = median_index + 1, median_index - 1
#         while len(result) != k:
#             if right_idx < n and left_idx >= 0:
#                 if abs(x - arr[right_idx]) < abs(x - arr[left_idx]):
#                     result.append(arr[right_idx])
#                     right_idx += 1
#                 else:
#                     result.appendleft(arr[left_idx])
#                     left_idx -= 1
#             else:
#                 if right_idx < n - 1:
#                     result.append(arr[right_idx])
#                     right_idx += 1
#                 elif left_idx >= 0:
#                     result.appendleft(arr[left_idx])
#                     left_idx -= 1
#     return list(result)
#
#
# def get_median_index(arr: List[int], x: int) -> int:
#     left, right = 0, len(arr) - 1
#     while left < right:
#         mid = (left + right) // 2
#         if arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid
#     if left > 0 and abs(arr[left - 1] - x) <= abs(arr[left] - x):
#         return left - 1
#     return left


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        diff = x - arr[mid]
        diff_k = arr[mid + k] - x
        if diff > diff_k:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]

print(findClosestElements(arr = [1,1,2,3,4,5], k = 4, x = -1))
