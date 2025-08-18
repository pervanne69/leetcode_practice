from typing import List


def removeCoveredIntervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda interval: (interval[0], -interval[1]))
    cur_interval = intervals[0]
    cur_start, cur_end = cur_interval
    result = len(intervals)
    for i in range(1, len(intervals)):
        now_start, now_end = intervals[i]
        if now_start >= cur_start and cur_end >= now_end:
            result -= 1
        else:
            cur_start, cur_end = now_start, now_end
    return result


print(removeCoveredIntervals(intervals = [[1,4],[2,3]]))