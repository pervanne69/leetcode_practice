def intervals_not(intervals):
    if not intervals:
        return 0
    intervals = list(sorted(intervals, key=lambda x: x[1]))
    count = 0
    last_end = -(10 ** 9)
    for i in range(len(intervals)):
        if last_end < intervals[i][0]:
            count += 1
            last_end = intervals[i][1]
    return count


print(intervals_not(intervals=[
    (1, 3),
    (2, 4),
    (3, 5),
    (6, 8),
    (7, 9),
]))
