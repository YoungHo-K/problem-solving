
from itertools import product
from bisect import bisect_left
from collections import defaultdict


def solution(info_list, query_list):
    info_list = [tuple(info.split(" ")) for info in info_list]
    query_list = [tuple(val for val in query.split(" ") if val != "and") for query in query_list]    

    score_dict = defaultdict(list)
    for info in info_list:
        for key in product(*tuple(('-', i) for i in info[:-1])):
            score_dict[key].append(int(info[-1]))
            
    for key in score_dict.keys():
        score_dict[key].sort()
            
    answer = list()
    for query in query_list:
        key, threshold = query[:-1], int(query[-1])

        answer.append(len(score_dict[key]) - bisect_left(score_dict[key], threshold))
    
    return answer
