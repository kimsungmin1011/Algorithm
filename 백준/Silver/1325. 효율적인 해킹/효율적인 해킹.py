# 1325_bfs_dp.py
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

# b 해킹 → a 해킹  ⇒  b → a 로 저장
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

# dp[i] : i번 컴퓨터에서 해킹 가능한 전체 수 (자기 자신 포함)
#  -1  : 아직 계산 안 됨
dp = [-1] * (n + 1)


def bfs(start):
    """start에서 해킹 가능한 컴퓨터 수를 리턴하고 dp[start]에 저장"""
    if dp[start] != -1:  # 이미 계산된 적이 있으면 바로 반환
        return dp[start]

    visited = [False] * (n + 1)  # BFS용 방문 배열
    visited[start] = True
    q = deque([start])
    cnt = 1  # 자기 자신까지 포함

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                cnt += 1
                q.append(nxt)

    dp[start] = cnt  # 캐싱
    return cnt


# 모든 정점에서 BFS 실행(필요한 경우에만)
best = 0
for i in range(1, n + 1):
    best = max(best, bfs(i))

# 가장 많이 해킹할 수 있는 정점(동률 가능) 출력
for i in range(1, n + 1):
    if dp[i] == best:
        print(i, end=" ")
