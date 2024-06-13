class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * (n + 1)
        for index in range(1, n + 1):
            dp[index] = max(dp[index - 1] + nums[index - 1], nums[index - 1])
        
        return max(dp[1:])