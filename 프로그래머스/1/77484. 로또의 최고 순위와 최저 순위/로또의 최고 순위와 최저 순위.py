def solution(lottos, win_nums):
    unknown = 0
    wins = 0
    for number in lottos:
        if number in win_nums:
            wins += 1
        
        if number == 0:
            unknown += 1
    
    win_to_rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}
    answer = []
    
    top = wins + unknown
    if top not in win_to_rank:
        answer.append(6)
    else:
        answer.append(win_to_rank[top])
        
    if wins not in win_to_rank:
        answer.append(6)
    else:
        answer.append(win_to_rank[wins])
    
    return answer