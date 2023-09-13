def solution(places):
    answer = []    
    for place in places:
        maps = [list(row) for row in place]

        is_good = 1
        for x in range(0, 5):
            for y in range(0, 5):
                if x + 2 < 5:
                    if (maps[x][y] == "P") and (maps[x + 2][y] == "P") and (maps[x + 1][y] != "X"):
                        is_good = 0
                        break
                
                if y + 2 < 5:
                    if (maps[x][y] == "P") and (maps[x][y + 2] == "P") and (maps[x][y + 1] != "X"):
                        is_good = 0
                        break
                
                if (x + 1 < 5) and (y + 1 < 5):
                    if (maps[x][y] == "P") and (maps[x + 1][y + 1] == "P") and ((maps[x + 1][y] != "X") or \
                            (maps[x][y + 1] != "X")):
                        is_good = 0
                        break

                    if (maps[x][y] == "P") and ((maps[x + 1][y] == "P") or (maps[x][y + 1] == "P")):
                        is_good = 0
                        break

                    if (maps[x + 1][y + 1] == "P") and ((maps[x + 1][y] == "P") or (maps[x][y + 1] == "P")):
                        is_good = 0
                        break
                        
                if (x == 4) and (y < 4):
                    if (maps[x][y] == "P") and (maps[x][y + 1] == "P"):
                        is_good = 0
                        break
                
                if (x < 4) and (y == 4):
                    if (maps[x][y] == "P") and (maps[x + 1][y] == "P"):
                        is_good = 0
                        break
                
                if (x > 0) and (y < 4):
                    if (maps[x][y] == "P") and (maps[x - 1][y + 1] == "P") and \
                                ((maps[x - 1][y] != "X") or (maps[x][y + 1] != "X")):
                        is_good = 0
                        break
                        
                if (y > 0) and (x < 4):
                    if (maps[x][y] == "P") and (maps[x + 1][y - 1] == "P") and \
                            ((maps[x][y - 1] != "X") or (maps[x + 1][y] != "X")):
                        is_good = 0
                        break
                
            if is_good == 0:
                break
                
        answer.append(is_good)
    
    return answer