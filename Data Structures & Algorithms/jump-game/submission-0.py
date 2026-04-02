class Solution:
    def canJump(self, nums: List[int]) -> bool:
        rng = nums[0]
        i = 1
        while i < len(nums) and rng > 0:
            rng -= 1
            rng = max(nums[i], rng)
            i += 1
        return i == len(nums)
