

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
        for i in range(0, n):            
            for j in range(i, n):
                substring = s[i: j + 1]
                                
                if is_palindrome(i, j) and ((answer is None) or (len(answer) < len(substring))):                    
                    answer = substring
        
        return answer
        