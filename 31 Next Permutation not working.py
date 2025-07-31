from typing import List

def nextPermutation(nums: List[int]):
    """
    Do not return anything, modify nums in-place instead.
    """
    nums_str = ''.join([str(i) for i in nums])
    integer = int(nums_str)
    while True:
        integer += 1
        if sorted(str(integer)) == sorted(nums_str):
            integer_list = [int(i) for i in str(integer)]
            for i in range(len(nums)):
                nums[i] = integer_list[i]
            break

nums = [1, 2, 3]
nextPermutation(nums)
print(nums)