from collections import deque

def solution(maps):
    answer = 0
    queue=deque([(0,0,1)])
    n,m=len(maps),len(maps[0])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    visited=[[False for _ in range(m)] for _ in range(n)]
    
    while queue:
        x,y,t=queue.popleft()
        visited[x][y]=True
        
        if x==n-1 and y==m-1:
            return t
        
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False and maps[nx][ny]==1:
                visited[nx][ny]=True
                queue.append((nx,ny,t+1))
            
    return -1