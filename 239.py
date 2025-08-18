from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    window = deque()
    result = []
    for i in range(len(nums)):
        while window and window[0] <= i - k:
            window.popleft()

        while window and nums[window[-1]] < nums[i]:
            window.pop()

        window.append(i)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result


print(maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))