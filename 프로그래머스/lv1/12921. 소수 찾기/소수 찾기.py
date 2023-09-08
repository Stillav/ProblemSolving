def solution(n):
    answer = 0
    
    prime_list = [i for i in range(2, n + 1)]
    answer_set = set(prime_list)
    for value in prime_list:
        delete_set = set([value * i for i in range(2, n//value + 1)])
        answer_set -= delete_set
        
    return len(answer_set) 