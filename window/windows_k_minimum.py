from typing import List
from collections import deque


# def k_min(nums: List[int], k: int) -> List[int]:
    # n = len(nums)
    # if k > n:
    #     return []
    # window = []
    # minimums = []
    #
    # for i in range(n):
    #
    #     while window and window[0] <= i - k:
    #         del window[0]
    #
    #     while window and nums[window[-1]] > nums[i]:
    #         window.pop()
    #
    #     window.append(i)
    #
    #     if i >= k - 1:
    #         minimums.append(nums[window[0]])
    # return minimums



def k_min(nums: List[int], k: int) -> List[int]:
    if k > len(nums):
        return []
    minimums = []
    window = deque()

    for i in range(len(nums)):
        while window and window[0] <= i - k:
            window.popleft()

        while window and nums[window[-1]] > nums[i]:
            window.pop()

        window.append(i)

        if i >= k - 1:
            minimums.append(nums[window[0]])

    return minimums



print(k_min(nums = [3, 2, 4, 6, 2, 3, 5, 7], k = 3))