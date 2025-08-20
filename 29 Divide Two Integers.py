def divide(dividend: int, divisor: int) -> int:
    sign = 1
    if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        sign = -1

    if dividend < 0:
        dividend *= -1
    if divisor < 0:
        divisor *= -1
    result = 0
    while dividend > divisor:
        dividend -= divisor
        result += 1
    result *= sign

    return result

print(divide(7, -3))