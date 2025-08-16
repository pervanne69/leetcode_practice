import heapq
from typing import List, Tuple




def sol2(intervals: List[Tuple[int, int]]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    heap = []
    heapq.heappush(heap, intervals[0][1])

    for i in range(1, len(intervals)):
        if heap[0] <= intervals[i][0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])

    return len(heap)


print(sol2(intervals = [(0,30),(5,10),(15,20)]))