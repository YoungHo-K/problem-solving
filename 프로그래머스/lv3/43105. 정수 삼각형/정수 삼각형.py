

def solution(triangle):
    dp = [[0] * length for length in range(1, len(triangle) + 1)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        values = triangle[i]
        
        dp[i][0] = dp[i - 1][0] + values[0]
        dp[i][-1] = dp[i - 1][-1] + values[-1]        
        
        for j in range(1, i):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + values[j]
        
    return max(dp[-1])