class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = deque()
        
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 2:
                    q.append([x, y])
                if grid[x][y] == 1:
                    fresh += 1

        while q and fresh:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= m or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    q.append([nx, ny])
                    fresh -= 1
            time += 1
                    
        return time if not fresh else -1

            
