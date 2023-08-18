global answer
global users
global emoticons


def solution(user_list, emoticon_list):
    global answer
    global users
    global emoticons
    
    answer = [0, 0]
    users = user_list
    emoticons = emoticon_list

    dfs(len(emoticons), [])
    
    return answer


def dfs(number_of_emoticons, sales):
    if number_of_emoticons == len(sales):
        calculate_answer(sales)
        
        return
    
    dfs(number_of_emoticons, sales + [10])
    dfs(number_of_emoticons, sales + [20])
    dfs(number_of_emoticons, sales + [30])
    dfs(number_of_emoticons, sales + [40])
    
    
def calculate_answer(sales):
    global answer
    global users
    global emoticons
    
    temp = [0, 0]
    for user_sale, user_price in users:
        total_price = 0
        for e, s in zip(emoticons, sales):
            if s >= user_sale:
                total_price += e * ((100 - s) / 100)
        
        if total_price >= user_price:
            temp[0] += 1
        else:
            temp[1] += total_price
    
    if answer[0] < temp[0]:
        answer = temp
        
    if (answer[0] == temp[0]) and (answer[1] < temp[1]):
        answer = temp


            