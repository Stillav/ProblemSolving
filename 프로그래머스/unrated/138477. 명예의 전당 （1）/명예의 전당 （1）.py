def solution(k, score):
    answer = []
    stack = []
    for num in score:
        stack.append(num)
        stack.sort(reverse=True)

        temp = stack[:k]
        answer.append(temp[-1])
        
    return answer