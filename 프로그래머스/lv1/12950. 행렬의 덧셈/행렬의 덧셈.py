def solution(arr1, arr2):
    import numpy as np 
    answer = np.array(arr1) + np.array(arr2)
    answer = answer.tolist()
    
    return answer