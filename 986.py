from typing import List


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    first = 0
    second = 0
    result = []
    while first < len(firstList) and second < len(secondList):
        first_start, first_end = firstList[first]
        second_start, second_end = secondList[second]
        start = max(first_start, second_start)
        end = min(first_end, second_end)
        if start <= end:
            result.append([start, end])
        if first_end < second_end:
            first += 1
        else:
            second += 1
    return result



print(intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))