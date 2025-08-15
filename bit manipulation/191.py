def hammingWeight(n: int) -> int:
    result = 0
    while n != 0:
        result += n & 1
        n >>= 1
    return result


print(hammingWeight(1000000001))
# 11 -> 1011
# 101
# 10
# 1
