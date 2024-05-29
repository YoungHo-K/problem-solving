from collections import defaultdict


def solution(X, Y):
    x_num = defaultdict(int)
    for x in X:
        x_num[x] += 1
        
    common_nums = []
    for y in Y:
        if x_num[y] > 0:
            common_nums.append(y)
            x_num[y] -= 1

    common_nums.sort(reverse=True)    
    if len(common_nums) == 0:
        return "-1"
    
    if common_nums[0] == "0":
        return "0"
    
    return "".join(common_nums)
    
