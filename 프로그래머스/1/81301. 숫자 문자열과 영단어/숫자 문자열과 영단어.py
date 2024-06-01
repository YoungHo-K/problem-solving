def solution(s):
    english_to_number = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    for word, num in english_to_number.items():
        s = s.replace(word, num)
        
    return int(s)