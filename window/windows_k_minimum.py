from typing import List


def k_min(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if k > n:
        return []
    window = []
    minimums = []

    for i in range(n):

        while window and window[0] <= i - k:
            del window[0]

        while window and nums[window[-1]] > nums[i]:
            window.pop()

        window.append(i)

        if i >= k - 1:
            minimums.append(nums[window[0]])
    return minimums

print(k_min(nums = [4, 2, 12, 3, 8, 1], k = 3))