def solution(number, limit, power):
    answer = 0
    
    for knight in range(1, number + 1):
        knight_power = calculate_power(knight)
        if limit < knight_power:
            knight_power = power
        
        answer += knight_power
    
    return answer


def calculate_power(number):
    count = 0
    for value in range(1, int(number ** 0.5) + 1):
        if number % value != 0:
            continue
        
        count += 1
        if value != (number // value):
            count += 1
            
    return count