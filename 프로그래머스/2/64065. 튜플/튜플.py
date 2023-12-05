from collections import defaultdict


def solution(s):
    freq_dict = defaultdict(int)
    for num in s.replace("{", "").replace("}", "").split(","):
        freq_dict[int(num)] += 1
    
    answer = [0] * len(freq_dict)
    for key, value in freq_dict.items():
        answer[value - 1] = key
    
    return answer[::-1]