from typing import List


def search(nums: List[int], target: int) -> int:
    return sol2(nums, target)


def sol1(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[left] <= nums[middle]:
            if nums[left] <= target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if nums[middle] <= target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
    return -1


def sol2(nums: List[int], target: int) -> int:
    # определим индекс минимального элемента
    n = len(nums)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    pivot = left

    left, right = 0, n - 1
    if nums[pivot] <= target <= nums[right]:
        left = pivot
    else:
        right = pivot - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(search(nums = [4,5,6,7,0,1,2], target = 0))