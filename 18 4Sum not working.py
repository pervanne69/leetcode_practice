from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n):
        if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right] + nums[left + 1]
            if total == target:
                res.append([nums[i], nums[left], nums[left + 1], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1] or nums[left - 1] == nums[left - 2] or nums[left] == \
                        nums[left - 2]:
                    left += 1
                while left < right and nums[right] == nums[right + 1] == nums[right + 2] or nums[right] == nums[
                    right + 1] or nums[right] == nums[right + 2]:
                    right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    return res


print(fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
