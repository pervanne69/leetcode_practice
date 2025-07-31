from collections import defaultdict



def subarraySum(nums, k: int) -> int:
    prefix_sum = 0
    count = 0
    count_map = defaultdict(int)
    count_map[0] = 1  # пустая сумма

    for num in nums:
        prefix_sum += num
        count += count_map[prefix_sum - k]
        count_map[prefix_sum] += 1

    return count

print(subarraySum([1,2,3], 3))