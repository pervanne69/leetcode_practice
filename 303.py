from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        prefix_sum = [0]
        for i in range(len(self.nums)):
            prefix_sum.append(prefix_sum[-1] + self.nums[i])
        return prefix_sum[right + 1] - prefix_sum[left]


numArr = NumArray([-2, 0, 3, -5, 2, -1])
print(numArr.sumRange(0,2))
