from typing import List


def findRightInterval(intervals: List[List[int]]) -> List[int]:
    starts = list(sorted([(intervals[i][0], i) for i in range(len(intervals))], key=lambda x: x[0]))  # nlogn
    n = len(starts)
    result = []
    for i in range(len(intervals)):  # n
        cur_interval_end = intervals[i][1]
        left = 0
        right = n - 1
        best = -1
        while left <= right:  # log n
            mid = (left + right) // 2
            if starts[mid][0] >= cur_interval_end:
                best = starts[mid][1]
                right = mid - 1

            else:
                left = mid + 1
        result.append(best)
    return result


print(findRightInterval([[3,4],[2,3],[1,2]]))