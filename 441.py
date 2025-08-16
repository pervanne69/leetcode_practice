def arrangeCoins(n: int) -> int:
    if n == 1:
        return 1
    def get_sum(num):
        return num * (num + 1) // 2

    left = 0
    right = n
    while left <= right:
        mid = (left + right) // 2
        if get_sum(mid) <= n:
            left = mid + 1
        else:
            right = mid - 1
    return right


print(arrangeCoins(6))