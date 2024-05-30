def solution(n):
    answer = n - 1
    for number in range(1, int(n ** 0.5) + 1):
        if n % number == 1:
            answer = number
            break
    
    return answer