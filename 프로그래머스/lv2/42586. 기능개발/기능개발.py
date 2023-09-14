def solution(progresses, speeds):

    answer = []
    
    while progresses:
        count = 0
        
        for i, progress in enumerate(progresses):
            progresses[i] = progress + speeds[i]
            
        while progresses and progresses[0] >= 100:
            count += 1 
            progresses.pop(0)
            speeds.pop(0)
            
        if count != 0:
            answer.append(count)
    
    return answer