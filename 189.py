from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    last_index = n - k
    first_index = 0
    while last_index < n:
        nums[first_index], nums[last_index] = nums[last_index], nums[first_index]
        first_index += 1
        last_index += 1

rotate(nums = [1,2,3,4,5,6,7], k = 3)