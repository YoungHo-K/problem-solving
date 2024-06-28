class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [-1] * n

        def dfs(start):
            if n <= start:
                return 0
        
            if dp[start] != -1:
                return dp[start]
        
            num_extra = float("inf")
            for value in dictionary:
                if s[start: start + len(value)] == value:
                    num_extra = min(num_extra, dfs(start + len(value)))

            num_extra = min(num_extra, dfs(start + 1) + 1)
        
            dp[start] = num_extra        
            return dp[start]
        
        return dfs(0)
