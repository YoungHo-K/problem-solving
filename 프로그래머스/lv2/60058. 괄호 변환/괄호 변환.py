def solution(p):
    answer = p if is_correct(p) is True else search(p)
    
    return answer


def search(w):
    if w == "":
        return w

    u = w
    v = ""
    count = [0, 0]
    for index in range(0, len(w)):
        if w[index] == "(": count[0] += 1
        else: count[1] += 1
        
        if count[0] == count[1]:
            u = w[: index + 1]
            v = w[index + 1: ]
            break
            
    if is_correct(u) is False:
        result = "(" + search(v) + ")" + get_inverse(u[1:-1])
    else:
        result = u + search(v)
    
    return result


def is_correct(s):
    stack = list()
    for val in s:
        if (len(stack) > 0) and (stack[-1] == "(") and (val == ")"):
            stack.pop()
            continue
            
        stack.append(val)
    
    return True if len(stack) == 0 else False


def get_inverse(s):
    inverse = list()
    for val in s:
        if val == "(": inverse.append(")")
        else: inverse.append("(")

    return "".join(inverse)