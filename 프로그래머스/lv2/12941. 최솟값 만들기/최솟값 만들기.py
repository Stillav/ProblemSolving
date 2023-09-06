def solution(A,B):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    A.sort()
    B.sort(reverse=True)
    
    for i, j in zip(A,B):
        answer += i * j

    return answer