class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
                   
        answer = []
        substrings = []

        def dfs(start):
            if start == n:
                answer.append(substrings.copy())                
                return
            
            for end in range(start, n):
                substr = s[start: end + 1]
                
                if substr == substr[::-1]:
                    substrings.append(substr)
                    dfs(end + 1)
                    substrings.pop()
            
        dfs(0)
        
        return answer
    