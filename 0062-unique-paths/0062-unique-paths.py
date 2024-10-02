class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [(0, 1), (1, 0)]
        
        dp = [[0] * n for _ in range(m)]
        for x in range(0, m):
            dp[x][0] = 1
        
        for y in range(0, n):
            dp[0][y] = 1
            
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = dp[x][y - 1] + dp[x - 1][y]
                
        return dp[m - 1][n - 1]
