class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1
        for x in range(n - 1, -1, -1):
            for y in range(m - 1, -1, -1):
                if x + 1 != n:
                    dp[y][x] += dp[y][x+1]
                if y + 1 != m:
                    dp[y][x] += dp[y + 1][x]
        return dp[0][0]
        