def solution(s):
    answer = True
    
    spell = list(s.lower())
    
    if not spell.count('p') == spell.count('y'):
        return False

    return True