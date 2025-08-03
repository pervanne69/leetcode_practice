from typing import List


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    left = 0
    n = len(nums)
    count = 0
    product = 1
    for right in range(n):
        product *= nums[right]
        while product >= k:
            product //= nums[left]
            left += 1
        count += right - left + 1
    return count


print(numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))