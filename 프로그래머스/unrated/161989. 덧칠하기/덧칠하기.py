def solution(n, m, section):
    answer = 1
    ref = section[0]
    
    for num in section:
        if ref + (m - 1) < num:
            ref = num
            answer += 1 
    return answer