def solution(new_id):
    new_id = new_id.lower()
        
    invalid_word = "~!@#$%^&*()=+[{]}:?,<>/"
    for word in invalid_word:
        new_id = new_id.replace(word, "")
    
    while new_id and ".." in new_id:
        new_id = new_id.replace("..", ".")
    
    if new_id and (new_id[0] == "."):
        new_id = new_id[1:]
    
    if new_id and (new_id[-1] == "."):
        new_id = new_id[:len(new_id) - 1]
            
    if len(new_id) == 0:
        new_id = "a"
        
    if len(new_id) >= 16:
        new_id = new_id[:15]

    if new_id[-1] == ".":
        new_id = new_id[:len(new_id) - 1]

    if len(new_id) < 3:
        while len(new_id) < 3:
            new_id += f"{new_id[-1]}"

    return new_id