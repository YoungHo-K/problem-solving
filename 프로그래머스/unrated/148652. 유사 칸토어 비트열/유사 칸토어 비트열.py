def solution(n, l, r):
    return count(n, r) - count(n, l - 1)


def count(n, k):
    if n == 1:
        return k if k <= 2 else k - 1
    
    length = 5 ** (n - 1)
    one_cnt = 4 ** (n - 1)
    loc = k // length

    if k % length == 0:
        loc -= 1
        
    if loc < 2:
        return one_cnt * loc  + count(n - 1, k - loc * length)
    
    elif loc == 2:
        return one_cnt * loc

    else:
        return one_cnt * (loc - 1) + count(n - 1, k - loc * length)
