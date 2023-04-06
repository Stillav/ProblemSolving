def solution(wallpaper):
    answer = []
    
    lux, luy, rdx, rdy = len(wallpaper), len(wallpaper[0]), 0, 0
    
    for x, row in enumerate(wallpaper):
        for y, char in enumerate(row):
            if char =="#":
                if x < lux:
                    lux = x
                if x + 1 > rdx:
                    rdx = x + 1 
                if y < luy:
                    luy = y 
                if y + 1> rdy:
                    rdy = y + 1
    answer = [lux, luy, rdx, rdy]            
    return answer