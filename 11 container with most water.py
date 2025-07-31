from typing import List


def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    maximum = 0
    while left < right:
        current = min(height[left], height[right]) * (right - left)
        maximum = max(maximum, current)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maximum


print(maxArea(height = [1,8,6,2,5,4,8,3,7]))
print(maxArea(height = [5,4,8,3,7]))
print(maxArea(height = [1,1]))