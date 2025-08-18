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


def sol1(intervals: List[Interval]) -> int:
    if not intervals:
        return 0

    d = dict()
    for interval in intervals:
        d[interval.start] = d.get(interval.start, 0) + 1
        d[interval.end] = d.get(interval.end, 0) - 1

    current_availble = 0
    max_availble = 0
    for point in sorted(d):
        current_availble += d[point]
        if current_availble > max_availble:
            max_availble = current_availble
    return max_availble


print(sol2(intervals = [(0,30),(5,10),(15,20)]))