from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        num_fresh_orange = 0
        rotten_oranges = []            
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j, 0))
                    
                elif grid[i][j] == 1:
                    num_fresh_orange += 1
                            
        answer = 0        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque(rotten_oranges)
        while queue:
            x, y, depth = queue.popleft()
            answer = max(answer, depth)
            
            for dx, dy in directions:
                next_x = x + dx
                next_y = y + dy
                
                if (0 <= next_x < m) and (0 <= next_y < n) and (grid[next_x][next_y] == 1):
                    queue.append((next_x, next_y, depth + 1))
                    grid[next_x][next_y] = 2
                    num_fresh_orange -= 1

        if num_fresh_orange > 0:
            return -1
                    
        return answer
        