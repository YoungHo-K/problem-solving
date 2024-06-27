from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(i, j):
            stack = [(i, j)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = "0"
                
                for dx, dy in directions:
                    next_x = x + dx
                    next_y = y + dy
                    
                    if (0 <= next_x < m) and (0 <= next_y < n) and (grid[next_x][next_y] == "1"):
                        stack.append((next_x, next_y))
        
        answer = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    answer += 1
                    
        return answer
    