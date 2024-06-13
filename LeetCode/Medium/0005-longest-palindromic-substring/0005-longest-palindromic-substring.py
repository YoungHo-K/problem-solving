

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[None] * n for _ in range(n)]

        def is_palindrome(start, end):
            if end <= start:
                return True
            
            if dp[start][end] is not None:
                return dp[start][end]
            
            if s[start] == s[end]:
                dp[start][end] = is_palindrome(start + 1, end - 1)
                
            else:
                dp[start][end] = False
                
            return dp[start][end]
        
        
        answer = None
        for length in range(n, 0, -1):            
            for index in range(0, n - length + 1):
                if is_palindrome(index, index + length - 1):
                    answer = s[index: index + length]
                    break
            
            if answer is not None:
                break
        
        return answer
        