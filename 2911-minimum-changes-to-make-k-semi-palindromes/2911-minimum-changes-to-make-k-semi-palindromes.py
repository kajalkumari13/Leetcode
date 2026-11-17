class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10**9
        divs = [[] for _ in range(n + 1)]
        for d in range(1, n + 1):
            for length in range(2 * d, n + 1, d):
                divs[length].append(d)

        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = INF
                for d in divs[length]:
                    m = length // d
                    cnt = 0
                    for r in range(d):
                        lo, hi = r, r + (m - 1) * d
                        while lo < hi:
                            if s[i + lo] != s[i + hi]:
                                cnt += 1
                            lo += d
                            hi -= d
                    best = min(best, cnt)
                cost[i][j] = best

        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for c in range(1, k + 1):
            for p in range(2 * c, n + 1):
                for q in range(2 * (c - 1), p - 1):
                    if dp[q][c - 1] < INF:
                        dp[p][c] = min(dp[p][c], dp[q][c - 1] + cost[q][p - 1])
        return dp[n][k]