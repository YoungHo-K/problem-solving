def solution(ingredient):
    answer = 0

    temp = []
    for value in ingredient:
        temp.append(value)
    
        if temp[-4: ] == [1, 2, 3, 1]:
            answer += 1
            
            for _ in range(0, 4):
                temp.pop()
    
    return answer