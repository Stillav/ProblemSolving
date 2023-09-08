def solution(N, stages):
    answer = []
    percent = dict()
    stages.sort()
    
    for i in range(1, N + 1):
        if len(stages) == 0:
            percent[i] = 0 
            continue
            
        count = stages.count(i)
        percent[i] = count / len(stages)
        
        for _ in range(count):
            stages.pop(0)
        
    percent_list = list(percent.items())
    percent_list.sort(key=lambda x: x[1], reverse=True)
    
    answer = [x[0] for x in percent_list]
    
    return answer