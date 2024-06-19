class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        
        def dfs(start):
            if n <= start:
                return 0
            
            answer = float("inf")
            if s[start] != "0":
                for end in range(start, n):
                    value = int(s[start: end + 1], 2)
                    while value % 5 == 0:
                        value //= 5
                        
                    if value == 1:
                        answer = min(answer, 1 + dfs(end + 1))
                        
            return answer
        
        answer = dfs(0)
        return -1 if answer == float("inf") else answer
        