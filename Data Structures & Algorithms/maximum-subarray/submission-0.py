class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(i):
            if i == len(nums):
                return 0
            curr = nums[i]
            a = dfs(i + 1)
            return max(curr, curr + a)
        res = nums[0]
        for j in range(len(nums)):
            res = max(res, dfs(j))
        return res
