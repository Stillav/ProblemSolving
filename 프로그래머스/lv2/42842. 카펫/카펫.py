def solution(brown, yellow):
    answer = []
    
    sum_wh = (brown + 4) // 2 
    
    for h in range(3, sum_wh // 2 + 1):
        if (h - 2) * (sum_wh - h - 2) == yellow:
            return [sum_wh - h ,h]
        
    return answer