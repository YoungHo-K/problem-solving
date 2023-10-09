
def solution(w, h):
    gcd = get_gcd(w, h)
    
    return w * h - gcd * (w / gcd + h / gcd - 1)


def get_gcd(x, y):
    if x % y == 0:
        return y
    
    return get_gcd(y, x % y)
        