from collections import deque
from typing import List


def getDistances(arr: List[int]):
    d = {}
    for i in range(len(arr)):
        if arr[i] in d:
            first_index = d[arr[i]].popleft()
            d[arr[i]].append(first_index)
            d[arr[i]].append(abs(first_index - i))
        else:
            d[arr[i]] = deque()
            d[arr[i]].append(i)
    result = []
    return d


print(getDistances(arr = [2,1,3,1,2,3,3]))