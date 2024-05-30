from collections import defaultdict


def solution(id_list, report, k):
    abuse_check = defaultdict(list)
    for r in report:
        user1, user2 = r.split(" ")
        
        abuse_check[user2].append(user1)
    
    answer = [0] * len(id_list)
    for target_user, report_users in abuse_check.items():
        report_users = set(report_users)
        
        if len(report_users) < k:
            continue
            
        for user in report_users:
            answer[id_list.index(user)] += 1
        
    return answer