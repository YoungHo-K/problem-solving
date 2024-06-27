from collections import deque


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[1e+9] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = grid[0][0]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = grid[i - 1][j - 1]                
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + cost, dp[i][j - 1] + cost)
                
        return dp[m][n]
        