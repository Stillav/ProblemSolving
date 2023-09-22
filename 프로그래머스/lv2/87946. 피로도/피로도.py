def solution(k, dungeons):
    from itertools import permutations 
    answer = 0

    for per_dungeons in permutations(dungeons, len(dungeons)):
        temp = 0
        temp_k = k
        for dungeon in per_dungeons:
            if temp_k >= dungeon[0]:
                temp_k -= dungeon[1]
                temp += 1 
                
        if temp > answer:
            answer = temp
    
    return answer