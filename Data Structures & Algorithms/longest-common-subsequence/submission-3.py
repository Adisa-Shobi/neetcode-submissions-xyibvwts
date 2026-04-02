class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        na, nb = len(text1), len(text2)
        memo = [[0] * (na + 1) for _ in range(nb + 1)]

        for a in range(na - 1, -1, -1):
            for b in range(nb - 1, -1, -1):
                if text1[a] == text2[b]:
                    memo[b][a] = 1 + memo[b + 1][a + 1]
                else:
                    memo[b][a] = max(memo[b + 1][a], memo[b][a + 1])
        return memo[0][0]

        
        