from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    left = 0
    nums_sorted = list(sorted([(nums[i], i) for i in range(len(nums))], key=lambda x: x[0]))
    right = len(nums) - 1
    while left < right:
        total = nums_sorted[left][0] + nums_sorted[right][0]
        if total == target:
            return [nums_sorted[left][1], nums_sorted[right][1]]
        else:
            if total > target:
                right -= 1
            else:
                left += 1


print(twoSum([2, 7, 11, 15], 9))


print(-1 or -2)