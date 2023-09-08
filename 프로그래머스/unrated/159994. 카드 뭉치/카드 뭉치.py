def solution(cards1, cards2, goal):
    
    answer = 'Yes'
    order = {word: i for i, word in enumerate(goal)}
    
    for word_index in range(len(cards1) - 1):
        
        if order.get(cards1[word_index], 21) > order.get(cards1[word_index + 1], 21):
            return 'No'
     
    for word_index in range(len(cards2) - 1):
        
        if order.get(cards2[word_index], 21) > order.get(cards2[word_index + 1], 21):
            return 'No'    

    return answer