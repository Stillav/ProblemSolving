def solution(priorities, location):
    answer = 0
    alphas = [chr(order) for order in range(ord('A'), ord('A') + len(priorities))]
    
    alphas_pair = [[key, value] for key, value in zip(alphas, priorities)]
    complete = []
    i = 1 
    while len(alphas_pair) != 0:
        max_priority = max(priorities)
        i += 1 
        if alphas_pair[0][1] != max_priority:
            alphas_pair.append(alphas_pair.pop(0))
        else:
            complete_value = alphas_pair.pop(0)
            complete.append(complete_value[0])
            priorities.remove(complete_value[1])
            
    answer = (complete.index(chr(ord('A') + location)) + 1)
    return answer