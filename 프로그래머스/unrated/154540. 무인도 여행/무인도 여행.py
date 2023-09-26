import sys

sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def solution(maps):
    def dfs(i,j):
        temp = 0
        if i < 0 or j < 0 or i >= len(maps) or j >= len(maps[0]):
            return temp
        
        if maps[i][j] != 'X' and vis[i][j] is False:
            vis[i][j] = True
            for num in range(4):
                temp += (dfs(i + dx[num], j + dy[num]))
                
            return int(maps[i][j]) + temp
        return temp
        
    answer = list()
    h = len(maps)
    w = len(maps[0])
    vis = [[False for _ in range(w)] for _ in range(h)]
    
    for i, row in enumerate(maps):
        for j, char in enumerate(row):
            if maps[i][j] != 'X' and vis[i][j] is False:
                answer.append(dfs(i,j))
    
    if len(answer) == 0:
        return [-1]
    
    answer.sort()
            
    return answer