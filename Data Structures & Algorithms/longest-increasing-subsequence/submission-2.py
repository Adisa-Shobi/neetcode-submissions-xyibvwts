class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, cnt, prev):
            if i == len(nums):
                return cnt
            # res = max(cnt, dfs(i+1, 0, 0))
            res = max(cnt, dfs(i+1, cnt, prev))
            if nums[i] > prev:
                res = max(res, dfs(i+1, cnt+1, nums[i]))
            return res
        return dfs(0, 0, float('-inf'))
