def solution(s):
    word_list = s.split(' ')
    
    for i, word in enumerate(word_list):
        temp = list()
        for j, spell in enumerate(word):
            if j % 2 == 0:
                temp.append(spell.upper())
            else:
                temp.append(spell.lower())
        word_list[i] = ''.join(temp)
    
    answer = ' '.join(word_list)
    
    return answer