from typing import List


def subarraysDivByK(nums: List[int], k: int) -> int:
    prefixes = {0: 1}
    current_sum = 0
    total = 0
    for num in nums:
        current_sum += num
        if current_sum % k in prefixes:
            total += prefixes[current_sum % k]
        prefixes[current_sum % k] = prefixes.get(current_sum % k, 0) + 1
    return total


print(subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))