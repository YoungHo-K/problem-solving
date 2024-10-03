class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        neighbor_directions = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]
        
        m, n = len(board), len(board[0])
        next_state = [[0] * n for _ in range(m)]
        for x in range(0, m):
            for y in range(0, n):
                next_state[x][y] = board[x][y]
                
                num_neighbors = 0                
                for dx, dy in neighbor_directions:
                    if (0 <= x + dx < m) and (0 <= y + dy < n):
                        num_neighbors += board[x + dx][y + dy]
                        
                if (board[x][y] == 0) and (num_neighbors == 3):
                    next_state[x][y] = 1

                if board[x][y] == 1:
                    if (num_neighbors < 2) or (num_neighbors > 3):
                        next_state[x][y] = 0
                    
                    else:
                        next_state[x][y] = 1
                        
        for x in range(0, m):
            for y in range(0, n):
                board[x][y] = next_state[x][y]
                        
