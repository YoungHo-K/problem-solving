def solution(a, b, g, s, w, t):
    left, right = 0, int(10 ** 16)
    
    while left <= right:
        middle = (left + right) // 2
        total, num_gold, num_silver = 0, 0, 0
        
        for gold, silver, weight, time in zip(g, s, w, t):
            move = middle // (time * 2)
            if middle % (time * 2) >= time:
                move += 1
            
            num_gold += weight * move if weight * move < gold else gold
            num_silver += weight * move if weight * move < silver else silver
            total += weight * move if weight * move < gold + silver else gold + silver

        if (num_gold >= a) and (num_silver >= b) and (total >= a + b):
            right = middle - 1
        else:
            left = middle + 1
    
    return left