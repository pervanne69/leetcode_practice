from typing import List


def numberOfArithmeticSlices(nums: List[int]) -> int:
    total = 0
    current = 0

    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            current += 1
            total += current
        else:
            current = 0

    return total

# print(numberOfArithmeticSlices(nums = [1,2,3,4]))
# print(numberOfArithmeticSlices(nums = [1,2,3,4,5]))
# print(numberOfArithmeticSlices([1, 2, 3]))
# print(numberOfArithmeticSlices([1,3,5,7,9]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))