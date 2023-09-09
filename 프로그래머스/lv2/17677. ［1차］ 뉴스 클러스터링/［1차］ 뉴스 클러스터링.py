def solution(str1, str2):
    answer = 0
    str1_dict, str2_dict = {}, {}
    inter, union = 0, 0
    
    for i in range(len(str1) - 1):
        if not str1[i:i+2].isalpha():
            continue
        temp = str1[i:i+2].lower()
        if str1_dict.get(temp) is None:
            str1_dict[temp] = 1 
        else:
            str1_dict[temp] += 1 
            
    for i in range(len(str2) - 1):
        if not str2[i:i+2].isalpha():
            continue
            
        temp = str2[i:i+2].lower()
        if str2_dict.get(temp) is None:
            str2_dict[temp] = 1 
        else:
            str2_dict[temp] += 1 
            
    for key in str1_dict:
        if str2_dict.get(key):
            inter += min(str1_dict.get(key), str2_dict.get(key))
            union += max(str1_dict.get(key), str2_dict.get(key))
        else:
            union += str1_dict[key]
        
    for key in str2_dict:
        if str1_dict.get(key):
            pass
        else:
            union += str2_dict[key]
    if not union:
        return 1 * 65536
    else:
        return int(inter / union * 65536)
    return answer