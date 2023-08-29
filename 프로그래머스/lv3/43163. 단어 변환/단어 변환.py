import copy

global answer


def solution(begin, target, words):
    global answer 
    answer = 51

    def dfs(current, word_list, depth):  
        global answer 
                
        if current == target:
            answer = depth if depth < answer else answer
            return            

        if len(word_list) == 0:
            return

        for w in word_list:
            if can_transform(current, w):
                next_words = copy.deepcopy(word_list)
                next_words.remove(w)
                
                dfs(w, next_words, depth + 1)
    
    dfs(begin, words, 0)
                
    if answer == 51:
        answer = 0
    
    return answer


def can_transform(x, y):
    diff = 0
    for val1, val2 in zip(x, y):
        if val1 != val2:
            diff += 1
    
    return True if diff == 1 else False