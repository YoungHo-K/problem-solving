def solution(rank, attendance):
    students = list()
    for index, (r, att) in enumerate(zip(rank, attendance)):
        if att is True:
            students.append((index, r))
    
    students.sort(key=lambda x: x[1])
    
    answer = 10000 * students[0][0] + 100 * students[1][0] + students[2][0]
    
    return answer