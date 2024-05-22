def solution(s):    
    answer = []

    char_to_index = {}
    for index, val in enumerate(s):
        if val not in char_to_index:
            answer.append(-1)
            char_to_index[val] = index
            continue
            
        answer.append(index - char_to_index[val])
        char_to_index[val] = index
    
    return answer