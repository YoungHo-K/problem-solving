def solution(array, commands):
    answer = []    
    for i, j, k in commands:
        tmp_arr = sorted(array[i - 1: j])
        answer.append(tmp_arr[k - 1])
    
    return answer