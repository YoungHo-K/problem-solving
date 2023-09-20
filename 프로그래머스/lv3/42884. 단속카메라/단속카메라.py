def solution(routes):
    routes.sort(key=lambda x: x[0])
    print(routes)
        
    answer = 0
    end_point = None
    for start, end in routes:
        if (end_point is None) or (end_point < start):
            end_point = end
            answer += 1
            continue
        
        if end < end_point:
            end_point = end
            
    return answer