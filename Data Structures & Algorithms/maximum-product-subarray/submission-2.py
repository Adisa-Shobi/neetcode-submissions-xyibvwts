class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1
        for n in nums:
            temp = n * currMax
            currMax = max(currMin * n, currMax * n, n)
            currMin = min(currMin * n, temp, n)
            res = max(res, currMax)
        return res
            