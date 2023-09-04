def solution(s):
    answer = True
    
    if len(s) in [4, 6] and s.isdigit():
        return True
        
    return False
