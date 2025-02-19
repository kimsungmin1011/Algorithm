from collections import deque

n, k = map(int, input().split())

visited = [False] * 100001  # 방문 여부를 저장할 리스트
queue = deque([(n, 0)])  # (위치, 경과 시간)

def bfs():
    while queue:
        x, time = queue.popleft()
        
        # 큐에서 꺼내면서 방문 처리
        visited[x] = True

        # 목표 위치에 도달하면 현재 시간을 반환
        if x == k:
            return time

        # 2 * x 위치로 이동 (시간이 0초 소요)
        if 0 <= 2 * x <= 100000 and not visited[2 * x]:
            queue.append((2 * x, time))
            visited[2 * x] = True

        # x + 1, x - 1 위치로 이동 (시간이 1초 소요)
        for nx in (x - 1, x + 1):
            if 0 <= nx <= 100000 and not visited[nx]:
                queue.append((nx, time + 1))
                visited[nx] = True

print(bfs())
