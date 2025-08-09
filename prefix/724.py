from typing import List


def pivotIndex(nums: List[int]) -> int:
    prefix = [0]
    for i in range(len(nums)):
        prefix.append(prefix[-1] + nums[i])
    # [0, 1, 8, 11, 17, 22, 28]
    for i in range(1, len(prefix)):
        left_sum = prefix[i - 1] if i != 0 else 0
        right_sum = prefix[-1] - prefix[i] if i != len(prefix) - 1 else 0
        if left_sum == right_sum:
            return i
    return -1


print(pivotIndex(nums = [1,2,3]))