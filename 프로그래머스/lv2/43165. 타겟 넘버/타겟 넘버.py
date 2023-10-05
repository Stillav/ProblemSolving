def solution(numbers, target):
    answer = 0
    
    def cal(index, temp_sum):
        nonlocal answer 
        
        if index == len(numbers):
            if temp_sum == target:
                answer += 1 
            return 
        
        cal(index+1, temp_sum + numbers[index])
        cal(index+1, temp_sum - numbers[index])
    
    cal(0, 0)
    return answer