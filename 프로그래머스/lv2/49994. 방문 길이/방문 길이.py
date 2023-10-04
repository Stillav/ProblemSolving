def solution(dirs):
    answer = 0
    x = y = 0 
    footprint = list()
    y_dict = {'U': 1, 'D': -1}
    x_dict = {'L': -1, 'R': 1}
    
    for pos in dirs:
        if abs(x + x_dict.get(pos, 0)) > 5 or abs(y + y_dict.get(pos, 0)) > 5:
            continue
        
        pos_x = x + x_dict.get(pos, 0)
        pos_y = y + y_dict.get(pos, 0)
        temp = sorted([[x, y], [pos_x, pos_y]])
        if temp not in footprint:
            footprint.append(temp)
        x = pos_x
        y = pos_y
        
    return len(footprint)