from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) :
    intervals.sort(key=lambda interval: (interval[1], interval[0]))
    cur_interval = intervals[0]
    cur_end = cur_interval[1]
    count = 0
    for i in range(1, len(intervals)):
        if cur_end > intervals[i][0]:
            count += 1
        else:
            cur_interval = intervals[i]
            cur_end = cur_interval[1]
    return count

print(eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))