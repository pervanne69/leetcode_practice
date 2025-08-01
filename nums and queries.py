from collections import Counter


def nums_and_queries(nums, queries):
    if not queries:
        return []
    if not nums and queries:
        return [0 for _ in range(len(queries))]
    n = len(nums)
    m = len(queries)
    counts = dict()
    for i in range(n):
        counts[nums[i]] = counts.get(nums[i], 0) + 1
    freq_count = Counter(counts.values())
    answer = [freq_count[q] if q in freq_count else 0 for q in queries]
    return answer


print(nums_and_queries(nums = [1, 2, 2, 3, 3, 3], queries = [2, 3, 2]))

#
# nums = [1, 2, 2, 3, 3, 3]
# queries = [1, 2, 3, 4]
# answer = [1, 1, 1, 0]