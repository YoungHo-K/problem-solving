def solution(left, right):
    answer = 0
    for number in range(left, right + 1):
        if get_length(number) % 2 == 0:
            answer += number
        else:
            answer -= number
        
    return answer


def get_length(number):
    count = 0
    for index in range(1, int(number ** 0.5) + 1):
        if number % index == 0:
            if number // index == index:
                count += 1
            else:
                count += 2
                            
    return count