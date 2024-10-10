class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')] * n
        
        def dfs(start):
            if start >= n:
                return 0
            
            if dp[start] != float('inf'):
                return dp[start]

            for end in range(start, n):
                substring = s[start: end + 1]
                if substring == substring[::-1]:
                    dp[start] = min(dp[start], dfs(end + 1) + 1)
            
            return dp[start]
        
        return dfs(0) - 1
                