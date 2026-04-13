class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        seen = set()
        res = [0]
        curr = [0]
        
        def dfs(x, y):
            if 0 > x or x >= n or 0 > y or y >= m or (x, y) in seen:
                return
            if grid[x][y] == 0:
                return
            curr[0] += 1
            res[0] = max(curr[0], res[0])
            seen.add((x, y))
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)
        
        for x in range(n):
            for y in range(m):
                curr[0] = 0
                dfs(x, y)
        return res[0]
            

