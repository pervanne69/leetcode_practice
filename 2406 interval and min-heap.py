import heapq
from typing import List


def minGroups(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda interval: interval[0])

    heap = []
    heapq.heappush(heap, intervals[0][1])

    for i in range(1, len(intervals)):
        if heap[0] < intervals[i][0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])

    return len(heap)

print(minGroups(intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]))