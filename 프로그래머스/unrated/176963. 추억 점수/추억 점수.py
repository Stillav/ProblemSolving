def solution(name, yearning, photo):
    answer = []
    
    score_translate = dict()
    
    for key, value in zip(name, yearning):
        score_translate.update({key: value})
        
    for p in photo:
        temp = 0
        for name in p:
            temp += score_translate.get(name, 0)
        answer.append(temp)
        
    print('hi')
    return answer