
from itertools import permutations


def solution(expression):
    operators = ["*", "+", "-"]
    operator_ranks = list(permutations(operators))

    answer = 0
    for rank in operator_ranks:
        first_op = rank[0]
        second_op = rank[1]
        
        rank_expression = list()
        for partial_expr in expression.split(first_op):
            temp_expr = [f"({value})" for value in partial_expr.split(second_op)]
            rank_expression.append(f"({second_op.join(temp_expr)})")
        
        price = eval(first_op.join(rank_expression))
        if answer < abs(price):
            answer = abs(price)
            
    return answer
