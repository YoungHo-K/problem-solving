def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    max_num = int(n * (n + 1) / 2)
    
    x = y = 0
    min_value = 1
    x_max = y_max = n - 1
    reverse = False
    for num in range(1, max_num + 1):
        answer[x][y] = num

        if x == x_max:
            if y == y_max:
                reverse = True
            else:
                y += 1
                continue

        if (reverse is True) and (x == min_value):
            min_value += 2
            x_max -= 1
            y_max -= 2
            reverse = False
        
        if reverse is True:
            x -= 1
            y -= 1
        else:
            x += 1
            
    return sum(answer, [])
        
    
        
        