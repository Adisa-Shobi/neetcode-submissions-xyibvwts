class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 0: 1}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            memo[i] = dfs(i - 1) + dfs(i - 2)
            return memo[i]
        return dfs(n)
