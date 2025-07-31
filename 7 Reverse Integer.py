


def reverse( x: int) -> int:
    str_x = str(x)
    sign = -1 if str_x[0] == "-" else 1
    if sign == -1:
        str_x = str_x[1:][::-1]
    else:
        str_x = str_x[::-1]
    result = int(str_x) * sign
    return result if -2 ** 31 <= result <= 2 ** 31 - 1 else 0


print(reverse(123))
print(reverse(-123))
print(reverse(0))
print(reverse(x = 120))