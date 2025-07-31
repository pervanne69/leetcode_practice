from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            k = j = middle
            while k - 1 >= 0 and nums[k - 1] == target:
                k -= 1
            while j + 1 < len(nums) and nums[j + 1] == target:
                j += 1
            return [k, j]
        else:
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
    return [-1, -1]


def searchRange(nums, target):
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
            if nums[mid] == target:
                first = mid
        return first

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            if nums[mid] == target:
                last = mid
        return last

    first = findFirst(nums, target)
    if first == -1:
        return [-1, -1]
    last = findLast(nums, target)
    return [first, last]


print(searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
