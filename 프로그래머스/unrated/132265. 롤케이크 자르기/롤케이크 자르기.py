def solution(topping):
    from collections import Counter 
    answer = 0
    bro = Counter(topping)
    young = set()
    for i in topping:
        bro[i] -= 1
        young.add(i)
        
        if bro[i] == 0:
            del bro[i]
        
        if len(bro) == len(young):
            answer += 1 
    return answer