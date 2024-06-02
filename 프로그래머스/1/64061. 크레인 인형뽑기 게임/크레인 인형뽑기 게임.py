from collections import defaultdict


def solution(board, moves):
    board_dict = defaultdict(list)
    for j in range(len(board[0])):
        for i in range(len(board) - 1, -1, -1):
            if board[i][j] != 0:
                board_dict[j].append(board[i][j])

    answer = 0
    stack = []
    for index in moves:
        if board_dict[index - 1]:
            value = board_dict[index - 1].pop()
            if stack and (stack[-1] == value):
                stack.pop()
                answer += 2                
            else:
                stack.append(value)
    
    return answer