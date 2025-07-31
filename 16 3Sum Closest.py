from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    closest = 10 ** 5
    n = len(nums)
    for i in range(n):
        left, right = i + 1, n - 1
        if left == i or right == i:
            continue
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(target - total) < abs(closest):
                closest = total
                right -= 1
            else:
                left += 1
                right -= 1
    return closest


print(threeSumClosest([10,20,30,40,50,60,70,80,90], target = 1))
print(threeSumClosest(nums = [-1,2,1,-4], target = 2))