def solution(keymap, targets):
    answer = []
    min_dict = {}
    for km in keymap:
        for i, spell in enumerate(km):
            if min_dict.get(spell) is None:
                min_dict[spell] = i + 1
            else:
                if min_dict[spell] > i + 1:
                    min_dict[spell] = i + 1
    
    for target in targets:
        temp = 0 
        for spell in target:
            if min_dict.get(spell) is None:
                temp = -1
                break
            temp += min_dict[spell]
        answer.append(temp)
        
    return answer