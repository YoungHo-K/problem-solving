def solution(players, callings):
    rank_to_player = {index: name for index, name in enumerate(players)}
    player_to_rank = {name: index for index, name in rank_to_player.items()}
    
    for name in callings:
        _rank = player_to_rank[name]
        _name = rank_to_player[_rank - 1]
        
        rank_to_player[_rank - 1] = name
        player_to_rank[name] = _rank - 1
        
        rank_to_player[_rank] = _name
        player_to_rank[_name] = _rank
            
    return list(rank_to_player.values())