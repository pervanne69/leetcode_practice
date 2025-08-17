from typing import List


def removeDuplicates(nums: List[int]) -> int:
    i = 0
    for j in range(len(nums)):
        if i < 2 or nums[j] != nums[i - 2]:
            nums[i] = nums[j]
            i += 1
    return i


print(removeDuplicates(nums = [1,1,1,2,2,3]))
