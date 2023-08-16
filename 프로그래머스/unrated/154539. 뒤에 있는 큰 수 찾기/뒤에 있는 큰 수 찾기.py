def solution(numbers):
    answer = [-1] * len(numbers)
    
    stack = list()
    for index in range(0, len(numbers)):  
        
        while stack and (stack[-1][1] < numbers[index]):
            pos, value = stack.pop()
            
            answer[pos] = numbers[index]
            
        stack.append((index, numbers[index]))
    
    return answer