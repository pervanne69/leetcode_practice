from collections import deque
from typing import List

# def k_max(nums: List[int], k: int) -> List[int]:
#     n = len(nums)
#     if k > n or k == 0:
#         return []
#
#     deq = deque()
#     max_windows = []
#
#     for i in range(n):
#         # Удаляем индексы, которые вышли за окно
#         while deq and deq[0] <= i - k:
#             deq.popleft()
#
#         # Удаляем из хвоста индексы элементов меньше текущего
#         while deq and nums[deq[-1]] < nums[i]:
#             deq.pop()
#
#         deq.append(i)
#
#         # Начинаем записывать максимум, когда окно достигло размера k
#         if i >= k - 1:
#             max_windows.append(nums[deq[0]])
#
#     return max_windows


def k_max(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if k > n:
        return []
    window_max = []
    max_windows = []
    for i in range(n):
        while window_max and window_max[0] <= i - k:
            del window_max[0]

        while window_max and nums[window_max[-1]] < nums[i]:
            window_max.pop()

        window_max.append(i)
        if i >= k - 1:
            max_windows.append(nums[window_max[0]])
    return max_windows


print(k_max(nums=[1, 3, -1, -3, 5, 3, 6, 7], k = 3))
