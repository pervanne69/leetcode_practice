from typing import List


def findDuplicate(nums: List[int]) -> int:
    low = 0
    high = len(nums) - 1
    while low < high:
        middle = (low + high) // 2
        count = 0
        for num in nums:
            if num <= middle:
                count += 1
        if count > middle:
            high = middle
        else:
            low = middle + 1
    return low

print(findDuplicate(nums = [1,3,4,2,2]))
