def solution(n, m):
    answer = []
    
    divisor = list()
    mul = 1
    if n > m:
        n, m = m, n
        
    for i in range(1, n + 1):
        while n % i == 0 and m % i == 0:
            divisor.append(i)
            
            if i == 1:
                break 
                
            n //= i
            m //= i
            
    
    for num in divisor:
        mul *= num
    
    answer.append(mul)
    answer.append(mul * n * m)
    print(answer)
    return answer