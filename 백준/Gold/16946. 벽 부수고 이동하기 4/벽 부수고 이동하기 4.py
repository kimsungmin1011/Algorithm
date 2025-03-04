from collections import deque

input = __import__("sys").stdin.readline


# 빈 공간(0)에서 연결된 모든 빈 공간을 같은 그룹으로 묶고 그 크기를 반환
def bfs(start):
    q = deque()
    q.append(start)
    cnt = 1
    while q:
        i, j = q.popleft()
        zeros[i][j] = group  # 해당 칸의 그룹 번호 할당
        for idx in range(4):
            ni, nj = i + dy[idx], j + dx[idx]
            if (
                ni < 0
                or ni >= n
                or nj < 0
                or nj >= m
                or visited[ni][nj]
                or graph[ni][nj] == 1
            ):
                continue
            visited[ni][nj] = True
            q.append((ni, nj))
            cnt += 1
    return cnt


n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 빈 공간의 그룹 번호를 저장하는 2차원 리스트
zeros = [[0] * m for _ in range(n)]

# 그룹의 크기를 저장하는 딕셔너리 (key = 번호, value = 크기)
info = {}
info[0] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

group = 1  # 빈 공간 그룹의 번호

# 빈 공간 그룹화 및 크기 계산
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            w = bfs((i, j))
            info[group] = w
            group += 1  # 그룹 번호 증가 (다음 그룹으로 넘어감)

# 벽 셀 값 업데이트
for i in range(n):
    for j in range(m):
        addList = set()  # 현재 칸에서 접촉하는 빈 공간 그룹의 번호 집합
        if graph[i][j] == 1:
            for idx in range(4):
                ni, nj = i + dy[idx], j + dx[idx]
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                addList.add(zeros[ni][nj])  # 접촉한 빈 공간 그룹 번호 추가

        # 현재 칸과 접촉한 빈 공간 그룹의 크기 더해줌
        for add in addList:
            graph[i][j] += info[add]  # info에서 각 그룹의 크기를 가져와 더함
            graph[i][j] %= 10

for g in graph:
    print("".join(map(str, g)))
