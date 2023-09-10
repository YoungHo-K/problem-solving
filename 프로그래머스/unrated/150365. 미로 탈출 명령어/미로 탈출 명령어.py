import heapq


def solution(n, m, x, y, r, c, k):
    directions = {"d": (1, 0), "u": (-1, 0), "l": (0, -1), "r": (0, 1)}    
    maps = [[0] * m for _ in range(0, n)]
    maps[r - 1][c - 1] = "E"

    answer = "impossible"
    heap = [("", x - 1, y - 1)]
    heapq.heapify(heap)
    while heap:
        route, x_pos, y_pos = heapq.heappop(heap)
        if maps[x_pos][y_pos] == "E":
            if len(route) == k:
                answer = route
                break
            
            if (k - len(route)) % 2 == 1:
                break
                
        if len(route) >= k:
            continue
            
        for direction, (dx, dy) in directions.items():
            next_x_pos = x_pos + dx
            next_y_pos = y_pos + dy
            if (next_x_pos < 0) or (n <= next_x_pos) or (next_y_pos < 0) or (m <= next_y_pos):
                continue
            
            if len(route) + 1 + abs(r - 1 - next_x_pos) + abs(c - 1 - next_y_pos) > k:
                continue
            
            heapq.heappush(heap, (route + direction, next_x_pos, next_y_pos))
        
    return answer

