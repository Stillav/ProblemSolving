def solution(sizes):
    answer = 0
    max_wh = [0, 0]
    for size in sizes:
        if size[0] < size[1]:
            temp = [size[1], size[0]]
        else:
            temp = size 
        
        if temp[0] > max_wh[0]:
            max_wh[0] = temp[0]
        
        if temp[1] > max_wh[1]:
            max_wh[1] = temp[1]
        
    return max_wh[0] * max_wh[1]