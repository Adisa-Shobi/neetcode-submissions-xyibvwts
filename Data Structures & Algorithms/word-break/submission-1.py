class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            
            sub = False
            for j in range(i, len(s) + 1):
                if s[i:j] in wordDict and dfs(j):
                    sub = True
            memo[i] = sub
            return sub
        return dfs(0)
