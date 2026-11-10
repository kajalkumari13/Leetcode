class Solution:
    def climbStairs(self, n, costs):
        INF = float('inf')
        p3, p2, p1 = INF, INF, 0
        for i in range(1, n + 1):
            cur = min(p1 + 1, p2 + 4, p3 + 9) + costs[i - 1]
            p3, p2, p1 = p2, p1, cur
        return p1