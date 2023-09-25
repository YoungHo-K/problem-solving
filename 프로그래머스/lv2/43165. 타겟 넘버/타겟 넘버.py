answer = 0

def solution(numbers, target):
    global answer
    
    dfs(numbers, 0, target, 0)
    
    return answer


def dfs(numbers, depth, target, value):
    if depth == len(numbers):
        if target == value:
            global answer
            answer += 1
        
        return
    
    dfs(numbers, depth + 1, target, value + numbers[depth])
    dfs(numbers, depth + 1, target, value - numbers[depth])    