from typing import List


def sol1(triangle: List[List[int]]) -> int:
    n = len(triangle)
    memo = [[10 ** 4 * n] * n for i in range(1, n + 1)]
    memo[0][0] = triangle[0][0]

    for i in range(1, n):
        for j, num in enumerate(triangle[i]):
            memo[i][j] = min(memo[i - 1][j], memo[i - 1][max(j - 1, 0)]) + triangle[i][j]
    return min(memo[-1])


def sol2(triangle: List[List[int]]) -> int:
    dp = triangle[-1][:]

    # Обрабатываем строки с конца к началу
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            print(triangle[i][j])
            print(min(dp[j], dp[j + 1]))
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

    return dp[0]


print(sol2([[2],[3,4],[6,5,7],[4,1,8,3]]))