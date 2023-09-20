def solution(X, Y):
    from itertools import zip_longest
    answer = []
    
    X_dict, Y_dict = dict(), dict()
    
    for X_num, Y_num in zip_longest(X,Y):
        if X_dict.get(X_num) is None:
            X_dict[X_num] = 1 
        else:
            X_dict[X_num] += 1 
            
        if Y_dict.get(Y_num) is None:
            Y_dict[Y_num] = 1
        else:
            Y_dict[Y_num] += 1 
    
    for num in X_dict:
        while X_dict.get(num) and Y_dict.get(num):
            answer.append(num)
            X_dict[num] -= 1
            Y_dict[num] -= 1 

    if len(answer) == 0:
        return "-1"
    
    answer.sort(reverse=True)
    
    if answer[0] == '0':
        return "0"
    
    answer = ''.join(answer)
    
    return answer