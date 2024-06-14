from collections import deque


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        for i in range(0, m):
            for j in range(0, n):
                if (board[i][j] == word[0]) and self.backtracking(board, word, i, j, 0):
                    return True

        return False
                
                
    def backtracking(self, board, word, i, j, length):
        if length == len(word):
            return True
        
        if not ((0 <= i < len(board)) and (0 <= j < len(board[0])) and (board[i][j] == word[length])):
            return False
        
        tmp_val = board[i][j]
        board[i][j] = ''
        
        if self.backtracking(board, word, i + 1, j, length + 1):
            return True

        if self.backtracking(board, word, i, j + 1, length + 1):
            return True

        if self.backtracking(board, word, i - 1, j, length + 1):
            return True

        if self.backtracking(board, word, i, j - 1, length + 1):
            return True
        
        board[i][j] = tmp_val
        
        return False
