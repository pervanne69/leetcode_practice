class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        right_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        for i in range(1, n - 1):
            current = height[i]
            total += max(0, min(left_max[i], right_max[i]) - current)
        return total



