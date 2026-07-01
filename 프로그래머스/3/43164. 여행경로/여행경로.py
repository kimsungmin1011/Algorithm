def solution(tickets):
    answer = []
    # tickets.sort()
    visited=[False for _ in range(len(tickets))] # 티켓 사용했는지
    
    route={} # 각 공항에서 갈 수 있는 곳
    for i in range(len(tickets)):
        s,d=tickets[i][0],tickets[i][1]
        if s not in route:
            route[s]=[i] # 티켓 번호 저장
        else:
            route[s].append(i)
    
    way=["ICN"]
    def dfs(current,count):
        flag=False
        if current in route:
            #지금 공항에서 쓸 수 있는 티켓 탐색
            for ticket in route[current]:
                if visited[ticket]==False:
                    flag=True
                    visited[ticket]=True
                    next=tickets[ticket][1] # 티켓에 나와있는 다음 목적지
                    way.append(next)
                    dfs(next,count+1)
                    visited[ticket]=False
                    way.pop()
                    
        if count==len(tickets):
            answer.append(way[:])
        
    dfs("ICN",0)
            
    return sorted(answer)[0]