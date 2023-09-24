def solution(s):
    answer = 0
    for index in range(0, len(s)):
        if check_string(s[index:] + s[:index]) is True:
            answer += 1

    return answer


def check_string(s):
    left = ["(", "[", "{"]
    right = [")", "]", "}"]
    
    stack = list()    
    for val in s:
        if val in left:
            stack.append(val)
            continue
        
        if (len(stack) > 0) and (stack[-1] == left[right.index(val)]):
            stack.pop()
        else:
            stack.append(val)
    
    return True if len(stack) == 0 else False