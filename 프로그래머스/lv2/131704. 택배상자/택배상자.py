def solution(order):
    answer = 0

    box = 1
    stack = list()
    while box <= len(order):
        stack.append(box)
        
        while stack and (stack[-1] == order[answer]):
            answer += 1
            stack.pop()
            
        box += 1
    
    return answer
