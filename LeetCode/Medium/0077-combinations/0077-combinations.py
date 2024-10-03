from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return list(map(list, combinations(range(1, n + 1), k)))
        answer = []
        
        visited = set()
        def dfs(start):
            if len(visited) == k:
                answer.append(list(visited))
                return
            
            for value in range(start + 1, n + 1):
                visited.add(value)
                dfs(value)
                visited.remove(value)
        
        dfs(0)
        
        return answer
