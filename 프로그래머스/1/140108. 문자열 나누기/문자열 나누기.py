def solution(s):
    answer = 0
    
    target = None
    same, differ = 0, 0
    for val in s:
        if target is None:
            target = val
            same += 1
            continue
        
        if val == target:
            same += 1
        else:
            differ += 1
        
        if same == differ:
            answer += 1
            target = None    
            
    if target is not None:
        answer += 1
    
    return answer