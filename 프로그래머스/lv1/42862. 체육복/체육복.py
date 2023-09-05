def solution(n, lost, reserve):
    answer = 0
    answer_dict = {i: 1 for i in range(1, n + 1)}
    reserve_ = list(set(reserve) - set(lost))
    lost_ = list(set(lost) - set(reserve))
    
    for num in reserve_:
        answer_dict[num] = 2
    
    for num in lost_:
        answer_dict[num] = 0
    
    for num in answer_dict:
        if answer_dict[num] == 0:
            if answer_dict.get(num - 1) == 2:
                answer_dict[num] = answer_dict[num - 1] = 1
                answer += 1
            elif answer_dict.get(num + 1) == 2:
                answer_dict[num] = answer_dict[num + 1] = 1
                answer += 1
        else:
            answer += 1
                
    
    return answer