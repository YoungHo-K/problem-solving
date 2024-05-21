def solution(park, routes):
    h, w = len(park), len(park[0])

    position = None
    for i in range(0, h):
        for j in range(0, w):
            if park[i][j] == "S":
                position = [i, j]
                
    for route in routes:
        direction, step = route.split(" ")
        
        if direction == "E":
            dx, dy = 0, 1
        
        elif direction == "W":
            dx, dy = 0, -1
            
        elif direction == "S":
            dx, dy = 1, 0
        
        else:
            dx, dy = -1, 0

        is_invalid = False
        for index in range(1, int(step) + 1):
            next_x = position[0] + dx * index
            next_y = position[1] + dy * index
                        
            if (next_x < 0) or (h <= next_x) or (next_y < 0) or (w <= next_y):
                is_invalid = True
                break

            if park[next_x][next_y] == "X":
                is_invalid = True
                break
        
        if not is_invalid:
            position = [next_x, next_y]
            
    return position