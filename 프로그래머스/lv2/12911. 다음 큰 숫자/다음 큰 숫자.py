def solution(n):
    answer = 0
    count_list = []
    cur = n 
    while n != 0:
        count_list.append(n % 2)
        n //= 2 
        
    while True:
        temp = cur + 1 
        cur += 1 
        temp_list = list()
        count_1 = count_list.count(1)
        while temp != 0:
            temp_list.append(temp % 2)
            temp //= 2 
            if temp_list.count(1) > count_1:
                break
        if temp_list.count(1) == count_1:
            return cur
        
        
    
    return answer