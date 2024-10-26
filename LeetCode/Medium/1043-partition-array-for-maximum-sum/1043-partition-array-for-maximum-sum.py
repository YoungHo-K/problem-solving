class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1] * n
                
        def search(start):
            if start >= n:
                return 0
            
            if dp[start] != -1:
                return dp[start]
        
            maximum_sum = 0        
            subarray_max_value = 0
        
            for index in range(start, min(n, start + k)):
                subarray_max_value = max(subarray_max_value, arr[index])
                
                maximum_sum = max(maximum_sum, subarray_max_value * (index - start + 1) + search(index + 1))
            
            dp[start] = maximum_sum
            
            return dp[start]
        
        return search(0)
