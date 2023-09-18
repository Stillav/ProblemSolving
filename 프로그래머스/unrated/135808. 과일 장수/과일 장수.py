def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    baguni = len(score) // m 
    
    for i in range(1, baguni + 1):
        answer += min(score[m * (i - 1):m * i]) * m

    
    return answer