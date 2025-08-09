class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        return sol2(nums)


def sol1(nums: List[int]) -> int:
    N = len(nums)
    INF = 10 ** 10

    @cache
    def run(idx, taken):
        if idx == N and taken:
            return -INF

        if idx == N:
            return 0

        if taken:
            return max(run(idx + 1, 1), nums[idx])

        return max(run(idx + 1, 0), -nums[idx] + run(idx + 1, 1))

    return run(0, 0)


def sol2(prices: List[int]) -> int:
    buy_price = prices[0]
    profit = 0
    for p in prices[1:]:
        if buy_price > p:
            buy_price = p
        profit = max(profit, p - buy_price)
    return profit
