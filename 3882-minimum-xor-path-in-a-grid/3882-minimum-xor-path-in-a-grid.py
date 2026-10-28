# Python

import sys
sys.setrecursionlimit(5000)

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        self.minVal = float('inf')

        # dp[i][j][curr] indicates whether this state
        # has already been explored.
        dp = [
            [[False] * 1024 for _ in range(n)]
            for _ in range(m)
        ]

        self.rec(grid, 0, 0, 0, dp)

        return self.minVal

    def rec(self, grid, i, j, curr, dp):
        m = len(grid)
        n = len(grid[0])

        # Out of bounds
        if i >= m or j >= n:
            return

        # Destination reached: include its value
        if i == m - 1 and j == n - 1:
            self.minVal = min(
                self.minVal,
                curr ^ grid[i][j]
            )
            return

        # This state has already been explored
        if dp[i][j][curr]:
            return

        dp[i][j][curr] = True

        # Include the current cell in the XOR
        nextXor = curr ^ grid[i][j]

        # Move right
        self.rec(grid, i, j + 1, nextXor, dp)

        # Move down
        self.rec(grid, i + 1, j, nextXor, dp)