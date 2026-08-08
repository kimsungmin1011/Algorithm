from collections import deque


def solution(storage, requests):
    original_n = len(storage)
    original_m = len(storage[0])

    # 창고 바깥에 빈 공간('x')을 한 겹 추가한다.
    #
    # ABC          xxxxx
    # DEF    ->    xABCx
    # GHI          xDEFx
    #              xGHIx
    #              xxxxx
    storage = (
        [['x'] * (original_m + 2)]
        + [['x'] + list(line) + ['x'] for line in storage]
        + [['x'] * (original_m + 2)]
    )

    # 바깥 공간을 추가한 후의 창고 크기
    n = original_n + 2
    m = original_m + 2

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(visited, pocket, value):
        # (0, 0)은 새로 추가한 바깥쪽 빈 공간이므로
        # 항상 외부에서 탐색을 시작할 수 있다.
        queue = deque([(0, 0)])
        visited[0][0] = True

        while queue:
            x, y = queue.popleft()

            for direction in range(4):
                nx = x + dx[direction]
                ny = y + dy[direction]

                if not (0 <= nx < n and 0 <= ny < m):
                    continue

                if visited[nx][ny]:
                    continue

                visited[nx][ny] = True

                # 요청한 컨테이너를 외부에서 발견한 경우
                # 바로 제거하지 않고 pocket에 저장한다.
                if storage[nx][ny] == value:
                    pocket.append((nx, ny))

                # 이미 비어 있는 공간이라면
                # 해당 공간을 통해 계속 이동한다.
                elif storage[nx][ny] == 'x':
                    queue.append((nx, ny))

    for request in requests:
        value = request[0]

        # 크레인 요청:
        # 외부 연결 여부와 관계없이 해당 종류를 전부 제거한다.
        if len(request) > 1:
            for i in range(1, n - 1):
                for j in range(1, m - 1):
                    if storage[i][j] == value:
                        storage[i][j] = 'x'

        # 지게차 요청:
        # 외부의 빈 공간과 연결된 컨테이너만 제거한다.
        else:
            pocket = []
            visited = [[False] * m for _ in range(n)]

            # 바깥에 추가한 빈 공간 (0, 0)에서 한 번만 탐색한다.
            bfs(visited, pocket, value)

            # 이번 탐색에서 접근할 수 있었던 컨테이너를 한꺼번에 제거한다.
            for x, y in pocket:
                storage[x][y] = 'x'

    answer = 0

    # 바깥에 추가한 테두리를 제외하고
    # 원래 창고 영역에 남아 있는 컨테이너만 센다.
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if storage[i][j] != 'x':
                answer += 1

    return answer