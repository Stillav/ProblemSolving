def solution(new_id):
    temp = []
    new_id = new_id.lower()
    for spell in new_id:
        if spell.isalpha() or spell.isdigit() or spell in ['-','_','.']:
            temp.append(spell)
    answer = ''.join(temp)
    while '..' in answer:
        answer = answer.replace('..','.')
        
    answer = answer.strip('.')
    
    if len(answer) == 0:
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')
        
    while len(answer) <= 2:
        answer += answer[-1]
        
    return answer