from typing import List

def longest_subarray_sum_k(nums: List[int], k: int) -> int:
    prefix_sum = 0
    prefix_indices = {0: -1}  # сумма 0 на позиции -1 (до начала массива)
    max_length = 0

    for i, num in enumerate(nums):
        prefix_sum += num
        if prefix_sum - k in prefix_indices:
            max_length = max(max_length, i - prefix_indices[prefix_sum - k])
        if prefix_sum not in prefix_indices:
            prefix_indices[prefix_sum] = i

    return max_length


print(longest_subarray_sum_k(nums = [1, -1, 5, -2, 3], k = 3))