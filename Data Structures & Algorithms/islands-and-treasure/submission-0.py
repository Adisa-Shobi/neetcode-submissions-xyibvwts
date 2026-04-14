class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        m, n = len(grid), len(grid[0])
        INF = 2147483647
        
        def dfs(x: int, y: int, dist: int):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == -1:
                return
            if dist >= grid[x][y]:   # No better distance
                return
            
            grid[x][y] = dist
            
            dfs(x + 1, y, dist + 1)
            dfs(x - 1, y, dist + 1)
            dfs(x, y + 1, dist + 1)
            dfs(x, y - 1, dist + 1)
        
        # Call DFS from every treasure
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    # Update 4 directions from treasure (distance starts at 1)
                    dfs(i + 1, j, 1)
                    dfs(i - 1, j, 1)
                    dfs(i, j + 1, 1)
                    dfs(i, j - 1, 1)