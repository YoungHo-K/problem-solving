from collections import defaultdict


def solution(nums):
    answer = 0
    
    pokemon_dict = defaultdict(int)
    for pokemon in nums:
        pokemon_dict[pokemon] += 1
        
    return min(len(pokemon_dict), len(nums) // 2)