def solution(left, right):
    answer = 0
    count_dict = {'odd': [], 'even': []}
    for num in range(left, right + 1):
        count = 1 
        for divisor in range(1, num // 2 + 1):
            if num % divisor == 0:
                count +=1 
        
        if count % 2 == 0:
            count_dict['even'].append(num)
        else:
            count_dict['odd'].append(num)
    answer = sum(count_dict['even']) - sum(count_dict['odd'])
    return answer