
from itertools import combinations
from collections import defaultdict


def solution(orders, course):    
    order_dict = defaultdict(list)
    for index, order in enumerate(orders):
        for val in order:
            order_dict[val].append(index)

    items = list(filter(lambda x: len(x[1]) > 1, order_dict.items()))           
    items = [item[0] for item in items]

    answer = list()
    for length in course:
        temp_answer = list()
        cnt = 2
        
        comb = set()
        for order in orders:
            if len(order) < length:
                continue
            
            order = list(order)
            order.sort()
            comb = comb | set(combinations(order, length))
        
        for menu in comb:
            menu_name = [menu[0]]
            menu_items = set(order_dict[menu[0]])
            
            for name in menu[1: ]:
                menu_name.append(name)
                menu_items = menu_items & set(order_dict[name])

            
            menu_name.sort()
            menu_name = "".join(menu_name)
            if cnt < len(menu_items):
                temp_answer = [menu_name]
                cnt = len(menu_items)
                
            elif cnt == len(menu_items):
                temp_answer.append(menu_name)
    
        answer.extend(temp_answer)

    answer.sort()
        
    return answer