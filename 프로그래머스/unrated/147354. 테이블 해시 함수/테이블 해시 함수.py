def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x: (x[col - 1], -x[0]))
    s = []
    
    for i in range(row_begin - 1, row_end):
        temp = 0
        for num in data[i]:
            temp += num % (i + 1) 
        s.append(temp)
        
    answer = s[0]
    
    for i in range(1, len(s)):
        answer ^= s[i]
    
    return answer