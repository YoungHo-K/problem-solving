class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]

        n = len(nums)
        visited = set()
        def dfs(index):
            for next_index in range(index + 1, n):
                visited.add(nums[next_index])
                answer.append(list(visited))
                dfs(next_index)
                visited.remove(nums[next_index])
        
        dfs(-1)
        
        return answer
        