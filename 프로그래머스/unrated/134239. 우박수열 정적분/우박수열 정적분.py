def solution(k, ranges):
    answer = []
    
    sequence = get_sequence(k)
    n = len(sequence) - 1
    for start, end in ranges:
        if end <= 0:
            end = n + end
        
        if end < start:
            answer.append(-1)
            continue
        
        answer.append(calculate_integral(sequence, start, end))
    
    return answer


def get_sequence(k):
    sequence = list()
    while True:
        sequence.append(k)
        if k == 1:
            break
            
        if k % 2 == 0:
            k /= 2
        else:
            k = k * 3 + 1
    
    return sequence


def calculate_integral(sequence, start, end):
    integral = 0.0
    for index in range(start, end):
        height = max(sequence[index], sequence[index + 1])
        
        integral += height - ((height - min(sequence[index], sequence[index + 1])) / 2)

    return integral        
        
        
        
        
        