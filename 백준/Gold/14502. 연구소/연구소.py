from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 벽 설치할 숫자 골랐으면 BFS로 탐색
def bfs(tlst):
    # [0] 3개 좌표를 1로 저장=> 벽 막기
    for i, j in tlst:
        arr[i][j] = 1

    # [1] 변수 및 큐 생성, 초기화
    q = deque()
    w = [[0] * M for _ in range(N)]  # BFS 방문배열
    cnt = len(lst) - 3  # 남은 0의 개수(max값 찾을 변수)

    for ti, tj in virus:
        q.append((ti, tj))
        w[ti][tj] = 1

    # [2] 큐에 데이터 있는 동안 한개 꺼내서 처리
    while q:
        ci, cj = q.popleft()
        # 네방향, 범위내, 미방문, 조건(==0)
        for i in range(4):
            ni, nj = ci + dx[i], cj + dy[i]
            if 0 <= ni < N and 0 <= nj < M and w[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                w[ni][nj] = 1
                cnt -= 1

    # [-1] 3개 좌표를 0로 저장 => 벽 해체
    for i, j in tlst:
        arr[i][j] = 0

    return cnt  # 남아있는 0(빈칸) 개수


# 벽 설치할 숫자 3개 조합으로 고르는 백트래킹 함수
def dfs(n, tlst, next):
    global ans
    if n == 3:  # 종료조건: 3개 숫자를 모두 선택완료
        ans = max(ans, bfs(tlst))
        return

    for j in range(next, len(lst)):
        dfs(n + 1, tlst + [lst[j]], j + 1)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# [1] 빈칸 위치, 바이러스 위치를 저장
lst = []
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            lst.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

ans = 0

# [1] 백트래킹 조합으로 풀이: 352mS
dfs(0, [], 0)
print(ans)
