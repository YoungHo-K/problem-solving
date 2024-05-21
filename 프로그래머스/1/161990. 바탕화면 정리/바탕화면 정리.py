def solution(wallpaper):
    lux, luy, rdx, rdy = len(wallpaper), len(wallpaper[0]), 0, 0
    
    for x, row in enumerate(wallpaper):
        for y, file in enumerate(row):
            if file == "#":
                lux, luy = min(lux, x), min(luy, y)
                rdx, rdy = max(rdx, x + 1), max(rdy, y + 1)

    return [lux, luy, rdx, rdy]