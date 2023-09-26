def solution(n):
    ans = 0
    left, right, tot = 0,0,0

    while left < n:
        if tot < n:
            right += 1 
            tot += right
        else:
            if tot == n: ans += 1 
            left += 1 
            tot -= left

    return ans