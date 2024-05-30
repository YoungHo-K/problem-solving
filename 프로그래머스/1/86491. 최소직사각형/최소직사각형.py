def solution(sizes):
    x, y = 0, 0
    for width, height in sizes:
        if width > height:
            x = max(width, x)
            y = max(height, y)
        
        else:
            x = max(height, x)
            y = max(width, y)
        
    return x * y
