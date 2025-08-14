from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals = list(sorted(intervals, key=lambda x: x[0]))
    cur_interval = intervals[0]
    cur_end = cur_interval[1]
    result = []
    for i in range(1, len(intervals)):
        next_interval = intervals[i]
        if cur_end >= next_interval[0]:
            cur_end = max(cur_end, next_interval[1])
        else:
            result.append([cur_interval[0], cur_end])
            cur_interval = intervals[i]
            cur_end = cur_interval[1]
    result.append([cur_interval[0], cur_end])
    return result


print(merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))