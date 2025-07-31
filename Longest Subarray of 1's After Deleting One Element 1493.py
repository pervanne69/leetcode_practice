class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not (0 in nums):
            return len(nums) - 1
        if not (1 in nums):
            return 0
        results = []
        result = 0
        for i in range(0, len(nums) - 1):
            if nums[i] == 1:
                result += 1
            else:
                if nums[i + 1] == 1:
                    if 0 in nums[i + 1:]:
                        result += nums.index(0, i + 1) - (i + 1)
                    else:
                        result += len(nums[i + 1:])
                results.append(result)
                result = 0
        for i in results:
            result = max(i, result)
        return result
