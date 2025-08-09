from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    first = float('inf')
    second = float('inf')

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True  # num > second > first -> found triplet

    return False


print(increasingTriplet(nums = [2,1,5,0,4,6]))
