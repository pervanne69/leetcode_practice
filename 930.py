from typing import List


def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    count = {0: 1}
    prefix_sum = 0
    result = 0
    for num in nums:
        prefix_sum += num
        if (prefix_sum - goal) in count:
            result += count[prefix_sum - goal]
        count[prefix_sum] = count.get(prefix_sum, 0) + 1
    return result



print(numSubarraysWithSum([1,0,1,0,1], goal = 2))

# 101
# 1010
# 0101
# 01010
# 010100
# 101
# 1010
# 10100
# 01