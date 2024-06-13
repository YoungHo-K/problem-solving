class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[None] * n for _ in range(n)]
        
        def is_palindromic(start, end):
            if end <= start:
                return True
            
            if dp[start][end] is not None:
                return dp[start][end]

            if s[start] == s[end]:
                dp[start][end] = is_palindromic(start + 1, end - 1)
            
            else:
                dp[start][end] = False
            
            return dp[start][end] 

        
        answer = 0
        for i in range(0, n):
            for j in range(i, n):
                if is_palindromic(i, j):
                    answer += 1
    
        return answer

    
        