from collections import deque
import sys

# 재귀 한도를 늘려 DFS를 깊게 탐색할 수 있도록 설정
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 역의 수 입력
n = int(input())

# 그래프 초기화: 각 역의 연결 정보를 저장할 인접 리스트
graph = [[] for _ in range(n + 1)]

# 순환선에 포함된 역들을 저장할 집합
cycle = set()

# 그래프 정보 입력 (역 a와 b가 연결되어 있음을 저장)
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 역의 방문 여부를 저장할 리스트
visited = [False] * (n + 1)

# 순환선이 이미 발견되었는지 여부를 나타내는 변수
cy = False


# DFS를 이용하여 순환선을 찾는 함수
def dfs(start, here, level, li):
    global cy
    # 순환선 여부를 찾기 전 2레벨까지는 일반 DFS 탐색
    if level <= 2:
        for v in graph[here]:
            if not visited[v]:
                visited[v] = True
                dfs(start, v, level + 1, li + [v])
                visited[v] = False
    else:
        for v in graph[here]:
            if not visited[v]:
                visited[v] = True
                dfs(start, v, level + 1, li + [v])
                visited[v] = False
            # 순환선 발견 조건: 시작점으로 돌아왔을 때
            elif v == start:
                cy = True  # 순환선이 있음을 표시
                for l in li:
                    cycle.add(l)  # 순환선에 포함된 역들을 cycle 집합에 저장
                return


# 각 역을 순환선 여부 확인 대상으로 DFS 수행
for i in range(1, n + 1):
    if cy:  # 순환선이 이미 발견된 경우 반복 종료
        break
    visited[i] = True
    dfs(i, i, 1, [i])
    visited[i] = False

# 순환선에 포함된 역들을 list로 변환
cycle = list(cycle)

# 각 역의 순환선까지의 거리를 저장할 리스트 초기화 (INF로 초기화)
answer = [int(1e9)] * (n + 1)

# BFS 초기화: 순환선에 속한 역의 거리는 0으로 설정
q = deque()
for c in cycle:
    q.append((c, 0))
    answer[c] = 0

# 순환선으로부터 다른 역까지의 거리 계산을 위한 BFS
while q:
    node, level = q.popleft()

    # 현재 역과 연결된 모든 역에 대해 거리 갱신
    for v in graph[node]:
        # 아직 방문하지 않은 역에 대해
        if answer[v] == int(1e9):
            answer[v] = level + 1  # 거리를 현재 레벨 + 1로 갱신
            q.append((v, level + 1))

# 각 역의 순환선까지의 거리 출력
for i in range(1, n + 1):
    print(answer[i], end=" ")
