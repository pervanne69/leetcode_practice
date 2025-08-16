


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals = list(sorted(intervals, key=lambda interval: (interval.start, interval.end)))
        if len(intervals) == 0:
            return True

        cur_end = intervals[0].end

        for i in range(1, len(intervals)):
            if cur_end > intervals[i].start:
                return False
            cur_end = intervals[i].end
        return True