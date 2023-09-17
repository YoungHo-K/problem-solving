import heapq

from collections import defaultdict


def solution(scores):
    heap = list()    
    score_dict = defaultdict(int)
    for index, (a, b) in enumerate(scores):
        score_dict[a] = max(b, score_dict[a])
        heapq.heappush(heap, (-(a + b), index))

    score_keys = list(score_dict.keys())
    score_keys.sort(reverse=True)
    
    answer = 0
    duplicate_count = 0
    score = None
    while heap:
        total_score, uid = heapq.heappop(heap)
        a, b = scores[uid]
        
        is_invalid = False
        for key in score_keys:
            if a >= key:
                break
            
            if b < score_dict[key]:
                is_invalid = True
                break
                
        if is_invalid is True:
            if uid == 0:
                answer = -1
                break
            else:
                continue
                    
        if score == total_score:
            duplicate_count += 1
        else:
            answer += duplicate_count + 1
            duplicate_count = 0
            score = total_score
            
        if uid == 0:
            break
            
    return answer