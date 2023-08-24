

def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    data = data[row_begin - 1: row_end]
    
    answer = 0
    for index, row in zip(range(row_begin, row_end + 1), data):
        mod_sum = 0
        for val in row:
            mod_sum += val % index
        
        answer = answer ^ mod_sum

    return answer