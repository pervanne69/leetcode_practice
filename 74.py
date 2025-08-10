from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    top, bottom = 0, m - 1
    while top <= bottom:
        mid_row = (top + bottom) // 2
        if matrix[mid_row][0] <= target <= matrix[mid_row][n - 1]:
            return check(matrix[mid_row], target)
        elif matrix[mid_row][0] > target:
            bottom = mid_row - 1
        else:
            top = mid_row + 1

def check(row: List[int], target: int) -> bool:
    left, right = 0, len(row) - 1
    while left <= right:
        mid = (left + right) // 2
        if row[mid] == target:
            return True
        elif row[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


print(searchMatrix(matrix = [[1]], target = 1))