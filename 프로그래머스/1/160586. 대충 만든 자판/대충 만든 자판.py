

def solution(keymap, targets):
    char_to_freq = {}
    for values in keymap:
        for index, c in enumerate(values):            
            if c not in char_to_freq:
                char_to_freq[c] = index + 1
            else:
                char_to_freq[c] = min(index + 1, char_to_freq[c])
            
    answer = []
    for target in targets:
        target_answer = 0
        for val in target:
            if val not in char_to_freq:
                target_answer = -1
                break
                
            target_answer += char_to_freq[val]
        
        answer.append(target_answer)
    
    return answer