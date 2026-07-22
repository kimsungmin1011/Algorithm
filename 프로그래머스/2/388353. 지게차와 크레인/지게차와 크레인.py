from collections import deque

def solution(storage, requests):
    storage=[list(line) for line in storage]
    answer = 0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    n=len(storage)
    m=len(storage[0])
    
    # 매 턴마다 끝자락에서 탐색 시작
    def bfs(visited,x,y,pocket,value):
        queue=deque([(x,y)])
        while queue:
            cx,cy=queue.popleft()
            for i in range(4):
                nx,ny=cx+dx[i],cy+dy[i]
                # 다음값이 현재값과 같거나 빈 공간이라면
                if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    if storage[nx][ny]==value:
                        pocket.append((nx,ny))
                    elif storage[nx][ny]=='x':
                        queue.append((nx,ny))
        
    
    for i in range(len(requests)):
        pocket=[]
        visited = [[False for _ in range(m)] for _ in range(n)]
        value=requests[i][0]
        
        # 알파벳이 두번 반복된 경우 크레인으로 외부에 연결되지 않은 컨테이너 꺼냄
        if len(requests[i])>1:
            for i in range(n):
                for j in range(m):
                    if storage[i][j]==value:
                        storage[i][j]='x'
                        
        # 알파벳이 한번만 주어진 경우 외부와 연결된 컨테이너 끌어냄                
        elif len(requests[i])==1:
            # 위아래에서 탐색 시작
            for start1 in range(n):
                bfs(visited,start1,-1,pocket,value)
                bfs(visited,start1,m,pocket,value)

            # 좌우측에서 탐색 시작
            for start2 in range(m):
                bfs(visited,-1,start2,pocket,value)
                bfs(visited,n,start2,pocket,value)

            # 접근 가능한 컨테이너 일거에 꺼냄
            for x,y in pocket:
                storage[x][y]='x'
    
    #남아있는 컨테이너 세기
    for i in range(n):
        for j in range(m):
            if storage[i][j]!='x':
                answer+=1
                
    return answer