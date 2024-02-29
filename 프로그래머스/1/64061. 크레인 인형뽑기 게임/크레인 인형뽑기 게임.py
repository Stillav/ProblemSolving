def solution(board, moves):
    answer = 0
    doll_stack = list()
    
    for move in moves:
        i = 0 
        while i < len(board) - 1 and board[i][move - 1] == 0:
            i += 1
        
        temp, board[i][move - 1] = board[i][move - 1], 0
        
        if temp == 0 and i == len(board) - 1:
            continue
        
        if len(doll_stack) != 0 and doll_stack[-1] == temp:
            answer += 2
            doll_stack.pop()
        else:
            doll_stack.append(temp)
        
    return answer