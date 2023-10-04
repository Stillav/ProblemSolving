def solution(storey):
    answer = 0
    
    while storey != 0:
        temp = storey % 10 
        storey //= 10 
        
        if temp < 5:
            answer += temp
        elif temp == 5:
            answer += (10 - temp)
            if storey % 10 >= 5:
                storey += 1                 
        else:
            answer += (10 - temp)
            storey += 1
    
    return answer