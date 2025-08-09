from typing import List


def numberOfSubarrays(nums: List[int], k: int) -> int:
    odd_count = 0
    left = 0
    count_arr = 0
    for right in range(len(nums)):
        if nums[right] % 2 != 0:
            odd_count += 1
        if odd_count == k:
            count_arr += 1
        elif odd_count > k:
            while odd_count != k:
                if nums[left] % 2 != 0:
                    odd_count -= 1
                    if odd_count == k:
                        count_arr += 1
                left += 1
    return count_arr

print(numberOfSubarrays(nums = [1,1,2,1,1], k = 3))