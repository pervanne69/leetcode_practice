from typing import List

def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = 3
    c = [0 for _ in range(k)]
    n = len(nums)
    for i in range(n):
        c[nums[i]] += 1
    b = 0
    for j in range(k):
        for i in range(c[j]):
            nums[b] = j
            b += 1


nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)