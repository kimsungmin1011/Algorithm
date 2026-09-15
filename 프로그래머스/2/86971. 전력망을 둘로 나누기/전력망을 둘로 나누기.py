from collections import deque

def solution(n, wires):
    answer = int(1e8)
    
    def bfs(idx,visited):
        q=deque([idx])
        count=1
        while q:
            current=q.popleft()
            for next in graph[current]:
                if visited[next]==False:
                    visited[next]=True
                    q.append(next)
                    count+=1
        return count
    
    
    for i in range(len(wires)):
        graph=[[] for _ in range(n+1)]
        # 전선 연결
        for j in range(len(wires)):
            # 전선 하나씩 끊어본다
            if i==j:
                continue
            graph[wires[j][0]].append(wires[j][1])
            graph[wires[j][1]].append(wires[j][0])
        
        # 네트워크 하나씩 탐색
        visited=[False for _ in range(n+1)]
        flag=False
        first,secound=0,0
        for k in range(1,n+1):
            if visited[k]==False:
                visited[k]=True
                # 첫번째 네트워크
                if flag==False:
                    flag=True
                    first=bfs(k,visited)
                # 두번째 네트워크
                else:
                    secound=bfs(k,visited)
                    
        answer=min(answer,abs(first-secound))
        
    return answer