def solution(data, ext, val_ext, sort_by):
    column_to_index = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    value_index = column_to_index[ext]
    sort_index = column_to_index[sort_by]
    answer = list(filter(lambda x: x[value_index] < val_ext, data))    
    answer.sort(key=lambda x: x[sort_index])

    return answer