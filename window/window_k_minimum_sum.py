from typing import List


def k_min_total(nums: List[int], k: int) -> int:
    n = len(nums)
    if k > n:
        return 0
    window = sum(nums[:k])
    mini = window
    for i in range(k, n):
        window = window - nums[i - k] + nums[i]
        if window < mini:
            mini = window

    return mini


print(k_min_total(nums = [5, 2, 7, 1, 3, 2, 6], k = 3))