from typing import List


def kthSmallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)

    def count_less_equal(x):
        count = 0
        i, j = 0, n - 1
        while i < n and j >= 0:
            if matrix[i][j] <= x:
                count += j + 1
                i += 1
            else:
                j -= 1
        return count

    left, right = matrix[0][0], matrix[-1][-1]
    while left < right:
        mid = (left + right) // 2
        if count_less_equal(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left


print(kthSmallest([[1, 2], [1, 3]], 2))
