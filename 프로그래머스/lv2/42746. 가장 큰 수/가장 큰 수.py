def solution(numbers):
    answer = ''
    numbers.sort(key=lambda x: str(x)*3, reverse=True)
    numbers = list(map(str, numbers))
    
    if numbers[0] == '0':
        return '0'
    
    answer = ''.join(numbers)
    return answer