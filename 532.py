from typing import List


def findPairs(nums: List[int], k: int) -> int:
    result = 0
    seen = set()
    nums.sort()
    for i in range(len(nums)):
        cur_num = nums[i]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid != i and checker(nums[mid], cur_num, k):
                if cur_num not in seen or nums[mid] not in seen:
                    result += 1
                    seen.add(cur_num)
                    seen.add(nums[mid])
                    break
            elif abs(cur_num - nums[mid]) > k:
                right = mid - 1
            else:
                left = mid + 1
    return result


def checker(a, b, target):
    return abs(a - b) == target


print(findPairs(nums = [3,1,4,1,5], k = 2))