def solution(numbers, hand):
    phone = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["*", "0", "#"]
    ]

    num_to_pos = {}
    for x in range(0, len(phone)):
        for y in range(0, len(phone[0])):
            num_to_pos[phone[x][y]] = (x, y)
    
    answer = ""
    last_dict = {"L": num_to_pos["*"], "R": num_to_pos["#"]}
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
        
        elif num in [3, 6, 9]:
            answer += "R"
            
        else:
            left_dist = sum([abs(x1 - x2) for x1, x2 in zip(num_to_pos[f"{num}"], last_dict["L"])])
            right_dist = sum([abs(x1 - x2) for x1, x2 in zip(num_to_pos[f"{num}"], last_dict["R"])])
            if left_dist == right_dist:
                answer += hand[0].upper()
                
            elif left_dist < right_dist:
                answer += "L"
            
            else:
                answer += "R"
                
        last_dict[answer[-1]] = num_to_pos[f"{num}"]
    
    return answer