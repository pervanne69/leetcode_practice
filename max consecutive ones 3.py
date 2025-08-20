from typing import List


def longest_ones(nums: List[int], k: int) -> int:
    left = 0
    zero_count = 0
    maxi = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while left <= right and zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        maxi = max(maxi, right - left + 1)

    return maxi
