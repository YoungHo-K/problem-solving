def solution(topping):
    left_topping_nums = get_unique_topping_nums(topping, 0, len(topping), 1)
    right_topping_nums = get_unique_topping_nums(topping, len(topping) - 1, -1, -1)

    
    answer = 0
    for index in range(0, len(topping) - 1):
        if left_topping_nums[index] == right_topping_nums[index + 1]:
            answer += 1
    
    return answer


def get_unique_topping_nums(topping, start, end, interval):
    topping_nums = [0] * len(topping)
    
    unique = set()
    for index in range(start, end, interval):
        unique.add(topping[index])
        
        topping_nums[index] = len(unique)
        
    return topping_nums