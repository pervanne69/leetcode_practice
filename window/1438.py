from collections import deque
from typing import List


def longestSubarray(nums: List[int], limit: int) -> int:
    max_dq = deque()
    min_dq = deque()
    left = 0
    result = 0

    for right in range(len(nums)):
        while max_dq and nums[right] > nums[max_dq[-1]]:
            max_dq.pop()
        max_dq.append(right)

        while min_dq and nums[right] < nums[min_dq[-1]]:
            min_dq.pop()
        min_dq.append(right)

        while nums[max_dq[0]] - nums[min_dq[0]] > limit:
            if max_dq[0] == left:
                max_dq.popleft()
            if min_dq[0] == left:
                min_dq.popleft()
            left += 1

        result = max(result, right - left + 1)

    return result



print(longestSubarray(nums = [10,1,2,4,7,2], limit = 5))