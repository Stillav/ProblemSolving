def solution(n):
    answer = 0
    count_one = bin(n).count('1')
    
    while True:
        n += 1 
        
        if bin(n).count('1') == count_one:
            break

    return n