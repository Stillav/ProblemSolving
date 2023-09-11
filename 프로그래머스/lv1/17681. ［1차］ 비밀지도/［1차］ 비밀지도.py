def solution(n, arr1, arr2):
    answer = [format(num1 | num2, 'b').replace('1', '#').replace('0', ' ').rjust(len(arr1)) for num1, num2 in zip(arr1, arr2)]
    return answer