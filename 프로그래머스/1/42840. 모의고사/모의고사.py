def solution(answers):
    acc = [0] * 3
    students = {
        0: [1, 2, 3, 4, 5],
        1: [2, 1, 2, 3, 2, 4, 2, 5],
        2: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    
    for index in range(0, len(answers)):
        for key, values in students.items():
            if answers[index] == (values[index % len(values)]):
                acc[key] += 1
    
    return [index for index in range(1, 4) if acc[index - 1] == max(acc)]