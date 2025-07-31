from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return 1
    nums = sorted(list(set(nums)))
    last = nums[0]
    count = 1
    max_length = 1
    n = len(nums)
    for i in range(1, n):
        if nums[i] - last == 1:
            last = nums[i]
            count += 1
            max_length = max(max_length, count)
        else:
            last = nums[i]
            count = 1
    max_length = max(max_length, count)
    return max_length


print(longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
print(longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(longestConsecutive(nums=[1, 0, 1, 2]))
