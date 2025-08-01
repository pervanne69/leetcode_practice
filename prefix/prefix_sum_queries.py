from typing import List
from collections import defaultdict

# def count_subarrays_with_sums(nums: List[int], queries: List[int]) -> List[int]:
#     prefix_sum = 0
#     prefix_count = defaultdict(int)
#     prefix_count[0] = 1  # сумма 0 встречается один раз
#     result_map = defaultdict(int)
#
#     for num in nums:
#         prefix_sum += num
#         for q in queries:
#             result_map[q] += prefix_count[prefix_sum - q]
#         prefix_count[prefix_sum] += 1
#
#     return [result_map[q] for q in queries]


def count_subarr_with_sums(nums: List[int], queries: List[int]):
    prefix_sum = 0
    prefix_count = {0: 1}
    result_map = {q: 0 for q in queries}

    for num in nums:
        prefix_sum += num
        for q in queries:
            target = prefix_sum - q
            if target in prefix_count:
                result_map[q] += prefix_count[target]
        if prefix_sum in prefix_count:
            prefix_count[prefix_sum] += 1
        else:
            prefix_count[prefix_sum] = 1

    return [result_map[q] for q in queries]





print(count_subarr_with_sums(nums=[1, 2, 1, 2, 1], queries=[3, 4]))
