def solution(arr):
    answer = []
    
    for num in arr:
        if len(answer) == 0:
            answer.append(num)
            continue
            
        if num != answer[-1]:
            answer.append(num)
        
    return answer