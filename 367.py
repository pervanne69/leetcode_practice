def isPerfectSquare(num: int) -> bool:
    left = 0
    right = num
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == num:
            return True
        elif mid * mid > num:
            right = mid - 1
        else:
            left = mid + 1
    return False




print(isPerfectSquare(4))