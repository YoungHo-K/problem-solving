class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] + [float("inf")] * (n - 1)
        
        for index in range(0, n):
            for jump in range(1, nums[index] + 1):
                if n <= index + jump:
                    continue
                
                dp[index + jump] = min(dp[index + jump], dp[index] + 1)
        
        return dp[-1]
                    