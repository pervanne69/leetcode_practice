from typing import List


def checkSubarraySum(nums: List[int], k: int) -> bool:
    prefix_mod = {0: -1}
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += num
        mod = prefix_sum % k
        if mod in prefix_mod:
            if i - prefix_mod[mod] > 1:
                return True

        prefix_mod[mod] = i
    return False


# nums = [23,2,4,6,7], k = 6

