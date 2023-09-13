def solution(clothes):
    answer = 1
    cloth_dict = dict()
    
    for cloth in clothes:
        if cloth_dict.get(cloth[1]):
            cloth_dict[cloth[1]] += 1
        else:
            cloth_dict[cloth[1]] = 1
            
    if len(cloth_dict) >= 2:
        for value in cloth_dict.values():
            answer *= (value + 1)
        
        return answer - 1
    else:
        for value in cloth_dict.values():
            
            return value