from collections import defaultdict
from typing import List


def prefix_sum_k_sequence(nums: List[int], k: int) -> List[int]:
    count = 0
    current_sum = 0
    prefix_sums = {0: 1}  # сумма 0 встречается 1 раз (пустой подмассив)

    for num in nums:
        current_sum += num
        if current_sum - k in prefix_sums:
            count += prefix_sums[current_sum - k]
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

    return count


print(prefix_sum_k_sequence(nums = [-2, -1, 2, 1], k = 1))
