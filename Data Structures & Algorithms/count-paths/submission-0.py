class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [0]
        def dfs(x, y):
            if x == n or y == m:
                return
            if x == (n - 1) and y == (m - 1):
                res[0] += 1
                return
            dfs(x+1, y)
            dfs(x, y+1)
        dfs(0,0)
        return res[0]
        