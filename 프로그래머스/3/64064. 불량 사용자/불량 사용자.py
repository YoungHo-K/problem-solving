from itertools import permutations


def is_banned_user(user, pattern):
    if len(user) != len(pattern):
        return False
    
    is_match = True
    for u, p in zip(user, pattern):
        if (p != "*") and (u != p):
            is_match = False
            break
    
    return is_match


def solution(user_id, banned_id):
    banned_users = dict()

    for user_list in permutations(user_id, len(banned_id)):
        match_count = 0
        for index in range(0, len(banned_id)):
            match_count += is_banned_user(user_list[index], banned_id[index])

        if match_count == len(banned_id):            
            banned_users[" ".join(sorted(user_list))] = 1

    return len(banned_users)