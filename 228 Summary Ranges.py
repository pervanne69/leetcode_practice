from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    if not nums:
        return []
    result = []
    current = 0
    low = 0
    n = len(nums)
    for i in range(0, n):
        if i == 0:
            low = current = nums[i]
        else:
            if nums[i] - current == 1:
                current = nums[i]
            else:
                if low == current:
                    result.append(str(current))
                else:
                    result.append(f"{low}->{current}")
                current = nums[i]
                low = nums[i]
        if i == n - 1:
            if low == current:
                result.append(str(current))
            else:
                result.append(f"{low}->{current}")
    return result


print(summaryRanges([0,2,3,4,6,8,9]))
