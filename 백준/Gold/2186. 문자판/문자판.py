import sys

input = sys.stdin.readline

# 입력
n, m, k = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
goal = list(input().strip())
L = len(goal)

#
# dp[x][y][idx]:
#   x, y 위치에서 goal[idx:] 부분 문자열을 완성할 수 있는 경로의 개수를 저장하는 메모이제이션 테이블
#   - 차원: n × m × L
#   - 값이 -1이면 '아직 계산되지 않음' 상태
dp = [[[-1] * L for _ in range(m)] for _ in range(n)]

#
# 상하좌우, 1~k칸 이동
# dx, dy 리스트:
#   네 방향(상, 하, 좌, 우)을 나타내며,
#   step만큼 곱해 다음 위치(nx, ny)를 계산할 때 사용
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


#
# dfs 함수 매개변수:
#   idx: 현재 목표 문자열(goal)의 몇 번째 글자를 찾고 있는지 나타내는 인덱스
#   x, y: 그래프 상에서 현재 탐색 중인 좌표
def dfs(idx: int, x: int, y: int):
    # 베이스 케이스: 목표 문자열 끝까지 탐색했다면 남은 부분이 없으므로 1개의 유효 경로로 간주
    if idx == L:
        return 1
    # 메모이제이션 체크:
    #   dp[x][y][idx]가 -1이 아니면 이전에 계산된 결과이므로 바로 반환하여 중복 계산 방지
    if dp[x][y][idx] != -1:
        return dp[x][y][idx]

    total = 0
    # 4방향 × 1~k칸
    for d in range(4):
        for step in range(1, k + 1):
            # d 변수: 방향 인덱스 (0:상,1:하,2:좌,3:우)
            # step: 1에서 k까지의 이동 거리
            nx = x + dx[d] * step
            ny = y + dy[d] * step
            # 다음 위치(nx, ny)가 범위 내에 있고, 목표 문자열의 현재 글자(goal[idx])와 일치하는지 검사
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == goal[idx]:
                total += dfs(idx + 1, nx, ny)

    dp[x][y][idx] = total
    return total


#
# 첫 글자가 일치하는 모든 좌표(i, j)를 출발점으로 설정
# 두 번째 글자(goal[1])부터 dfs를 호출하여 전체 경로 수 누적
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == goal[0]:
            answer += dfs(1, i, j)

print(answer)
