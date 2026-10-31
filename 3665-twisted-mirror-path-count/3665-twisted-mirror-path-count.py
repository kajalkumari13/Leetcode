class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[[-1] * 2 for _ in range(n)] for _ in range(m)]

        def help(r, c, d):
            if r == m - 1 and c == n - 1:
                return 1

            if r >= m or c >= n:
                return 0

            if dp[r][c][d] != -1:
                return dp[r][c][d]

            if grid[r][c] == 1:
                if d == 0:
                    dp[r][c][d] = help(r + 1, c, 1)
                else:
                    dp[r][c][d] = help(r, c + 1, 0)
            else:
                dp[r][c][d] = (
                    help(r + 1, c, 1) +
                    help(r, c + 1, 0)
                ) % MOD

            return dp[r][c][d]

        return help(0, 0, 0)