from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        sum_value = 0
        dp = defaultdict(int)
        dp[0] += 1
        
        for value in nums:
            sum_value += value            
            if (sum_value - k) in dp:
                answer += dp[sum_value - k]
                
            dp[sum_value] += 1    
            
        return answer