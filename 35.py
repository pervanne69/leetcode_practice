def searchInsert(nums: list, target: int) -> int:
    if target in nums:
        return nums.index(target)
    if target < nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)
    for i in range(len(nums)):
        if nums[i] > target:
            return i

print(searchInsert(nums = [1,3,5,6], target = 5))
print(searchInsert(nums = [1,3,5,6], target = 2))
print(searchInsert(nums = [1,3,5,6], target = 7))
print(searchInsert(nums = [1,3,5,6], target = 0))