import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r, q = map(int, input().split())  # (트리 정점 수 N, 루트 번호 R, 쿼리 수 Q)

graph = [[] for _ in range(n + 1)]

# 무방향 트리 간선 정보 저장
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [-1] * (n + 1)  # 각 정점을 루트로 하는 서브트리에 속한 정점의 개수

# 정점 U 저장
root = []
for _ in range(q):
    root.append(int(input()))


def dfs(x):
    dp[x] = 1  # dp 기본값 1 (자기 자신을 정점으로 가짐)

    # 연결된 정점 DFS 탐색
    for next in graph[x]:
        if dp[next] == -1:  # 연결된 정점이 아직 방문하지 않았다면
            dp[x] += dfs(next)  # 현재 dp에 연결된 정점의 dp값 더해줌

    return dp[x]  # 탐색 끝나고 현재 dp값 반환


# 루트 R에서부터 탐색 시작
dfs(r)

# 저장된 정점을 루트로 하는 서브트리에 속한 정점의 수 (dp[i]) 출력
for i in root:
    print(dp[i])
