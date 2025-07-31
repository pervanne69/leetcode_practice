from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    most_frequent = dict()
    result = []
    for i in nums:
        most_frequent[i] = most_frequent.get(i, 0) + 1
    most_frequent = sorted(most_frequent.items(), key=lambda x: x[1], reverse=True)
    for i in range(k):
        result.append(most_frequent[i][0])
    return result


print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(topKFrequent(nums = [1], k = 1))