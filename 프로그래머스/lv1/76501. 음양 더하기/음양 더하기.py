def solution(absolutes, signs):
    answer = 0
    
    for value, sign in zip(absolutes, signs):
        answer += value if sign else -value
    return answer