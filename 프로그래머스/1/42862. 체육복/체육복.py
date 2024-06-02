def solution(n, lost, reserve):
    reserve_student = []
    for student in sorted(reserve):
        if student in lost:
            lost.remove(student)
            continue
            
        reserve_student.append(student)
    
    for student in reserve_student:
        if student - 1 in lost:
            lost.remove(student - 1)
            continue
                        
        if student + 1 in lost:
            lost.remove(student + 1)
            continue
    
    return n - len(lost)
        
    
    
    

