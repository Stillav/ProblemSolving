def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    for i, citation in enumerate(citations, start=1):
        if i <= citation:
            answer = i
            
    
    return answer