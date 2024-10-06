class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        
        for index in range(0, m):
            if obstacleGrid[index][0] == 1:
                break
                
            dp[index][0] = 1
            
        for index in range(0, n):
            if obstacleGrid[0][index] == 1:
                break
                
            dp[0][index] = 1
        
        
        for x in range(1, m):
            for y in range(1, n):
                if obstacleGrid[x][y] == 1:
                    continue
                
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
                
        return dp[-1][-1]
    