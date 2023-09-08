def solution(players, callings):
    answer = []
    
    player_dict = {key : i+1 for i, key in enumerate(players)}
    ranking_dict = {i+1 : key for i, key in enumerate(players)}
    
    for player in callings:
        player_dict[player] -=1
        
        front_player = ranking_dict[player_dict[player]]
        
        player_dict[front_player] += 1 
        
        ranking_dict[player_dict[player]] = player
        ranking_dict[player_dict[player] + 1] = front_player
        
    answer = list(ranking_dict.values())
    
    return answer