def solution(cap, n, deliveries, pickups):
    answer = 0
    
    number_of_delivery = 0
    number_of_pickup = 0
    for index in range(n, 0, -1):
        number_of_delivery += deliveries[index - 1]
        number_of_pickup += pickups[index - 1]
        
        while (number_of_delivery > 0) or (number_of_pickup > 0):
            number_of_delivery -= cap
            number_of_pickup -= cap
            
            answer += index * 2
    
    return answer