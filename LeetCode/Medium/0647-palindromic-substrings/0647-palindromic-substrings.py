class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        answer = 0
        for length in range(1, n + 1):
            for index in range(0, n - length + 1):
                substring = s[index: index + length]
                
                if substring == substring[::-1]:
                    answer += 1
    
        return answer
