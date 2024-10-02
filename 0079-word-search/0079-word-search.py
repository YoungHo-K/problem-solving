class Solution:
    answer = False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(x, y, visited):
            if len(visited) == len(word):
                self.answer = True
                return
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for dx, dy in directions:
                next_x = x + dx
                next_y = y + dy
                
                if (0 <= next_x < m) and (0 <= next_y < n) and ((next_x, next_y) not in visited) and \
                    (board[next_x][next_y] == word[len(visited)]):

                    visited.add((next_x, next_y))
                    dfs(next_x, next_y, visited)
                    visited.remove((next_x, next_y))
        
        for x in range(0, m):
            for y in range(0, n):
                if board[x][y] == word[0]:
                    dfs(x, y, set([(x, y)]))
                    
        return self.answer