def solution(n):
    n_3str = ""
    while n:
        n_3str += f"{n % 3}"
        n = n // 3

    answer = 0
    for index, num in enumerate(n_3str[::-1]):
        answer += int(num) * (3 ** index)
            
    return answer