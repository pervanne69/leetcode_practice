from typing import List


def jump(nums: List[int]) -> int:
    max_reach = 0
    count = 0
    n = len(nums)
    end = 0
    for i in range(n - 1):
        max_reach = max(max_reach, i + nums[i])
        if i == end:
            count += 1
            end = max_reach
    return count



print(jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))