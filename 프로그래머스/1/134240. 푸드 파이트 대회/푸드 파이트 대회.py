def solution(food):
    answer = ''    
    for index, count in enumerate(food[1: ]):
        answer += f"{index + 1}" * (int(count) // 2)
        
    answer = answer + "0" + answer[::-1]
    
    return answer