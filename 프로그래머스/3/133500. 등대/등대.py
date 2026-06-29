import sys
sys.setrecursionlimit(10**6)

def solution(n, lighthouse):    
    # dp[x][0] = 불 안 켰을 때 x의 서브트리에 필요한 불 켜진 등대
    # dp[x][1] = 불 켰을 때 x의 서브트리에 필요한 불 켜진 등대
    dp=[[-1,-1] for _ in range(n+1)]
    visited=[False for _ in range(n+1)]
    graph=[[] for _ in range(n+1)]
    
    for x,y in lighthouse:
        graph[x].append(y)
        graph[y].append(x)
        
    def dfs(node):
        visited[node]=True
        dp[node][0]=0
        dp[node][1]=1
        for next in graph[node]:
            if visited[next]==False:
                dfs(next)
                dp[node][0]+=dp[next][1]
                dp[node][1]+=min(dp[next])
    
    dfs(1)
    
    answer = min(dp[1])
    return answer