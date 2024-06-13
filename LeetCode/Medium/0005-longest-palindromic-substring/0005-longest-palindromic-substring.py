

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        answer = None
        for length in range(n, 0, -1):
            
            for index in range(0, n - length + 1):
                substring = s[index: index + length]
                
                left = 0
                right = length - 1
                
                is_palindromic = True
                while left < right:
                    if substring[left] != substring[right]:
                        is_palindromic = False
                        break
                    
                    left += 1
                    right -= 1
                                    
                if is_palindromic:
                    answer = substring
                    break
            
            if answer is not None:
                break
        
        return answer
        