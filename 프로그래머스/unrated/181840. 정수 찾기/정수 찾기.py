def solution(num_list, n):
    num_list.append(n)
    
    return 0 if num_list.index(n) == len(num_list) - 1 else 1