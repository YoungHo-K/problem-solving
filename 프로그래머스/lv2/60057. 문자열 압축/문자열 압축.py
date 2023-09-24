def solution(s):
    answer = float("inf") if len(s) != 1 else 1
    
    for length in range(1, len(s) // 2 + 1):
        count = 1
        index = length
        value = s[:index]

        string = ""        
        while index < len(s):
            next_value = s[index: index + length]
            if value == next_value:
                count += 1
            else:
                string += f"{count}{value}" if count > 1 else f"{value}"
                value = next_value
                count = 1
                
            index += length
        
        string += f"{count}{value}" if count > 1 else f"{value}"
        if len(string) < answer:
            answer = len(string)        
        
    return answer