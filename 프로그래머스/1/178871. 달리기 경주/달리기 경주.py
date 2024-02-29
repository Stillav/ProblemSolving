def solution(players, callings):
    rank_dict, player_dict = dict(), dict()
    
    for i, player in enumerate(players):
        rank_dict[i + 1] = player
        player_dict[player] = i + 1
    
    for call in callings:
        rank = player_dict[call]
        previous_palyer = rank_dict[rank - 1]
        player_dict[call] -= 1
        player_dict[previous_palyer] += 1 
        rank_dict[rank - 1] = call
        rank_dict[rank] = previous_palyer
    
    return list(rank_dict.values())