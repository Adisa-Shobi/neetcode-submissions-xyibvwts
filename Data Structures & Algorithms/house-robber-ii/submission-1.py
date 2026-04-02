class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memoA = {}
        memoB = {}
        n = len(nums)
        def dfs(i, m, memo):
            if i in memo:
                return memo[i]
            if i >= m:
                return 0
            
            skip = dfs(i + 1, m, memo)
            noSkip = nums[i] + dfs(i + 2, m, memo)
            memo[i] = max(skip, noSkip)
            return memo[i]
        return max(dfs(0,  n - 1, memoA), dfs(1, n, memoB))