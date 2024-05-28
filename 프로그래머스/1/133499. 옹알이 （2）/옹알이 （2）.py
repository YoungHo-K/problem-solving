

def solution(babbling):
    use_words = ["aya", "ye", "woo", "ma"]
        
    answer = 0    
    for word in babbling:
        if word in use_words:
            answer += 1
            continue
        
        prev = ""
        curr = ""
        for w in word:
            curr += w
            
            if (prev != curr) and (curr in use_words):
                prev = curr
                curr = ""
                continue
            
        if curr == "":
            answer += 1
    
    return answer