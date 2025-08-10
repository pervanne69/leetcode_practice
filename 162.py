from typing import List


def findPeakElement(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid == 0:
            if nums[mid] > nums[mid + 1]:
                return mid
            left += 1
        elif mid == len(nums) - 1:
            if nums[mid] > nums[mid - 1]:
                return mid
            right -= 1
        else:
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    right = mid - 1


print(findPeakElement(nums = [2, 1]))

