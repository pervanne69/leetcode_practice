# Input: nums = [1, 3, -1, 5, 7, -3], k = 3
# Output: 11  # (5 + 7 + -3 = 9), но (3 + -1 + 5 = 7), но (1+3+(-1)=3),
# но (1+3+(-1)=3), (3+(-1)+5=7), (1+3+(-1)=3) → 11 из (3+(-1)+5)=7, (−1+5+7)=11


def window_k_sums(nums, k):
    n = len(nums)
    if k > n:
        return 0
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, n):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    return max_sum



print(window_k_sums(nums = [1, 3, -1, 5, 7, -3], k = 3))
print(window_k_sums(nums = [4, 2, 1, 6], k = 2))
