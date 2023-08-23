def solution(brown, yellow):
    areas = get_yellow_area(yellow)
    print(areas)
    
    answer = None
    for row, column in areas:
        number_of_brown = 4 + 2 * row + 2 * column
        if number_of_brown == brown:
            answer = [column + 2, row + 2]
            break
        
    return answer


def get_yellow_area(yellow):
    areas = list()
    for num in range(1, yellow + 1):
        if yellow % num != 0:
            continue
            
        if num <= yellow // num:
            areas.append((num, yellow // num))
        else:
            break
    
    return areas
            
        