def solution(board, h, w):    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    answer = 0
    for dx, dy in directions:
        now_x = h + dx
        now_y = w + dy
        
        if (now_x < 0) or (len(board) <= now_x):
            continue
            
        if (now_y < 0) or (len(board) <= now_y):
            continue
        
        if board[h][w] == board[now_x][now_y]:
            answer += 1
            
    return answer