def solution(arr):
    answer = 1

    for value in arr:
        gcd = get_gcd(answer, value)
        
        answer = answer * value / gcd
    
    return answer


def get_gcd(x, y):
    if x % y == 0:
        return y
    
    return get_gcd(y, x % y)