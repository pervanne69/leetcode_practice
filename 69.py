def mySqrt(x: int) -> int:
    left = 0
    right = x
    while left < right:
        mid = (left + right + 1) // 2
        if checkIsSquareRoot(mid, x):
            left = mid
        else:
            right = mid - 1
    return left


def checkIsSquareRoot(mid, x):
    if mid ** 2 <= x:
        return True
    return False



print(mySqrt(4))