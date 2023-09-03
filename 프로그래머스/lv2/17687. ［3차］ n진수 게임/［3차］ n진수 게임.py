def solution(n, t, m, p):
    positions = [p + m * i for i in range(0, t)]
    
    num = 0
    string = ''
    while len(string) <= positions[-1]:
        string += transform(num, n)
        num += 1
        
    answer = ''
    for pos in positions:
        answer += string[pos - 1]
        
    return answer


def transform(num, n):
    string = ''
    num_to_alpha = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    while True:
        div, mod = num // n, num % n
            
        string += str(mod) if mod < 10 else num_to_alpha[mod]
        num = div
        
        if div == 0:
            break
        
    return string[::-1]