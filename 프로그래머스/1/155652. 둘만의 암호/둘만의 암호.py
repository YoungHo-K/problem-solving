def solution(s, skip, index):
    skip = [ord(val) for val in skip]
    
    answer = ''
    for val in s:
        val = ord(val)
        
        move = 0        
        while move < index:
            val += 1
            if val > 122:   # 'z'
                val = 97    # 'a'
            
            if val in skip:
                continue
            
            move += 1
            
        answer += chr(val)
    
    return answer