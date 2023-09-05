def solution(nums):
    import itertools 
    
    answer = 0
    
    sum_list = list(map(sum,itertools.combinations(nums, 3)))

    for num in sum_list:
        is_prime = True 
        for i in range(2, num// 2 + 1):
            if num % i == 0:
                is_prime = False
                break
                
        answer += int(is_prime)

    return answer