import math


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        
        answer = [None]
        def dfs(start, depth):
            if n <= start:
                if (answer[0] is None) or (depth < answer[0]):
                    answer[0] = depth
                
                return
            
            if s[start] != "0":
                for end in range(start, n):
                    value = int(s[start: end + 1], 2)
                    while value % 5 == 0:
                        value //= 5
                                        
                    if value == 1:
                        dfs(end + 1, depth + 1)

        dfs(0, 0)            
                        
        return -1 if answer[0] is None else answer[0]