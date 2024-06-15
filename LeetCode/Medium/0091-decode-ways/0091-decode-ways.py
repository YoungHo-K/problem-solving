class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        
        def dfs(index):
            if n <= index:
                return 1
            
            if dp[index] != -1:
                return dp[index]
            
            answer = 0
            if s[index] != "0":
                answer += dfs(index + 1)
                if (index + 1 < n) and (10 <= int(s[index] + s[index + 1]) <= 26):
                    answer += dfs(index + 2)
            
            dp[index] = answer
            return dp[index]
        
        return dfs(0)
            