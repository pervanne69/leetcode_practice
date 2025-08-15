class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        return sol1(0, n)

def sol1(result, n: int):
    if 2 << result == n:
        return True
    if 2 << result > n:
        return False
    return sol1(result + 1, n)