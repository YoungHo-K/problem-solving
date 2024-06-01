def solution(dartResult):
    area_to_bonus = {"S": 1, "D": 2, "T": 3}
    
    answer = []    
    current = ""
    for d in dartResult:
        if d.isdigit():
            if isinstance(current, int):
                answer.append(current)
                current = ""
            
            current += d
            continue
        
        current = int(current)
        
        if d in area_to_bonus:
            current = current ** area_to_bonus[d]
        
        if d == "*":
            current *= 2
            if len(answer) > 0:
                answer[-1] *= 2
        
        if d == "#":
            current *= -1
    
    answer.append(current)

    return sum(answer)