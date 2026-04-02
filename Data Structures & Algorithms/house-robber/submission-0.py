class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1
        booty = {n : nums[n]}
        
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in booty:
                return booty[i]
            
            y = nums[i] + dfs(i + 2)
            n = dfs(i + 1)
            booty[i] = max(y, n)
            return booty[i]
        return dfs(0)
        