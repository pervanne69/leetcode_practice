from typing import List


def count_k_multiplicity(nums: List[int], k: int) -> int:
    prefix_multiplicities = {0: 1}
    count = 0
    current_multiplicity = 0

    for num_index in range(len(nums)):
        current_multiplicity += nums[num_index]
        if current_multiplicity % k in prefix_multiplicities:
            count += prefix_multiplicities[current_multiplicity % k]
        prefix_multiplicities[current_multiplicity % k] = prefix_multiplicities.get(current_multiplicity % k, 0) + 1
    return count



print(count_k_multiplicity(nums = [-4, -5, 0, -2, -3, 1], k = 5))

