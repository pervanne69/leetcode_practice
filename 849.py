class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        right_dist = [float("inf") for _ in range(n)]
        left_dist = [float("inf") for _ in range(n)]
        last_seated = float("-inf")
        for i in range(n):
            if seats[i] == 1:
                last_seated = i
            if seats[i] == 0 and last_seated != float("-inf"):
                left_dist[i] = i - last_seated

        last_seated = float("-inf")
        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                last_seated = i
            if seats[i] == 0 and last_seated != float("-inf"):
                right_dist[i] = last_seated - i
        maxi = 0
        for i in range(n):
            if seats[i] == 0:
                maxi = max(maxi, min(left_dist[i], right_dist[i]))
        return maxi