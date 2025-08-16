from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    return sol2(nums, target)


def sol2(nums: List[int], target: int) -> List[int]:
    left_bound, right_bound = -1, -1
    n = len(nums)
    left, right = 0, n - 1
    # ищем левую границу
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
        if nums[mid] == target:
            left_bound = mid

    # ищем правую границу
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
        if nums[mid] == target:
            right_bound = mid

    return [left_bound, right_bound]


def sol1(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            low = high = mid
            while low - 1 >= 0 and nums[low - 1] == target:
                low -= 1
            while high + 1 <= len(nums) - 1 and nums[high + 1] == target:
                high += 1
            return [low, high]
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return [-1, -1]

print(searchRange(nums = [5,7,7,8,8,10], target = 8))

# [5 7 7 8 8 10]
# n = 6
# left = 0 right = 5
# mid = 2
# nums[2] < target = 8 => left = mid + 1 = 3

# left = 3 right = 5
# mid = 4
# nums[4] = target => low = high = 4
# low - 1 = 3 >= 0 and nums[low - 1 = 3] == target: low -= 1
# low = 3
# high + 1 = 5 <= len(nums) and nums[high + 1 = 5] = 10 != target => high = 4
# return [low, high]


# # [1 1]
# left = 0
# right = 1
# mid = 0
# low = high = 0
# low - 1 = -1 < 0 => low = 0
# high + 1 = 1 <= len(nums) - 1 = 1 and nums[high + 1 = 1] = 1 = target => high = 1
