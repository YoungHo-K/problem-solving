
def solution(arrayA, arrayB):
    answer = 0
    answer = max(find_a(arrayA, arrayB), answer)
    answer = max(find_a(arrayB, arrayA), answer)
    
    return answer


def find_a(arrayA, arrayB):
    gcd = None
    for index in range(0, len(arrayA)):
        if gcd is None:
            gcd = arrayA[index]
            continue
            
        gcd = get_gcd(gcd, arrayA[index])
        
    if gcd == 1:
        return 0

    is_divide = False
    for val in arrayB:
        if val % gcd == 0:
            is_divide = True
            break
            
    return gcd if is_divide is False else 0


def get_gcd(x, y):
    if x % y == 0:
        return y
    
    return get_gcd(y, x % y)
    