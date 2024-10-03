class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        n = len(nums)
        visited = []
        def dfs():
            if len(visited) == n:
                answer.append(list(visited))
                return
            
            for index in range(0, n):
                if nums[index] not in visited:
                    visited.append(nums[index])
                    dfs()
                    visited.pop()
                    
        dfs()
        
        return answer
                