from itertools import product


def solution(word):
    vowels = [["A", "E", "I", "O", "U"]]

    dictionary = list()
    for length in range(1, 6):
        values = list(product(*(vowels * length)))
        
        for w in values:
            dictionary.append("".join(w))

    dictionary.sort()            
            
    return dictionary.index(word) + 1