def isPowerOfFour(n: int) -> bool:
    if n == 1:
        return True
    return sol1(0, n)


def sol1(result, n: int):
    if 4 << result == n and result % 2 == 0:
        return True
    if 4 << result > n:
        return False
    return sol1(result + 1, n)


for i in range(-2 ** 31, 2 ** 31 + 1):
    print(isPowerOfFour(i))
