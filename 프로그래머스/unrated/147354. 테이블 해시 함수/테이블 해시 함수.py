import heapq


def solution(data, col, row_begin, row_end):
    # if len(data) == 1:
    #     return sum(data[0]) ^ sum(data[0])
        
    sorted_data = list()
    for row in data:
        pivot = col - 1        
        new_data = [row[pivot], -row[0]] + row[1: pivot] + row[pivot + 1:] 
        
        heapq.heappush(sorted_data, new_data)

    index = 0
    answer = None
    while sorted_data and (index < row_end):
        data = heapq.heappop(sorted_data)
        
        index += 1
        if index < row_begin:
            continue
                
        data[1] *= -1
        mod_sum = 0
        for val in data:
            mod_sum += val % index

        answer = mod_sum if answer is None else answer ^ mod_sum
    
    return answer