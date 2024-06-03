def solution(n, arr1, arr2):
    answer = []
    for index in range(n):
        _map = bin(arr1[index] | arr2[index])[2:]
        _map = _map.replace("1", "#").replace("0", " ")
        answer.append(" " * (n - len(_map)) + _map)
    
    return answer