n = int(input())  # 맵 크기
k = int(input())  # 사과개수

graph = [[0 for _ in range(n)] for _ in range(n)]
# 사과위치
for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1

# 방향 바꾸는 시간, 방향
change = dict()
l = int(input())
for _ in range(l):
    x, d = input().split()
    change[int(x)] = d  # x초가 끝난 뒤 d 방향으로 바꿈

cx, cy, cd, time = 0, 0, 0, 1
snake = [(0, 0)]
# 동,남,서,북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    nx, ny = cx + dx[cd], cy + dy[cd]
    if (0 <= nx < n and 0 <= ny < n and (nx, ny) not in snake) != True:
        break

    cx, cy = nx, ny  # 뱀 머리위치 이동
    snake.append((cx, cy))
    if graph[cx][cy] != 1:
        snake.pop(0)
    else:
        graph[cx][cy] = 0

    # time초가 끝난 후 방향 변환(방향 변환 정보에 있을 시)
    if time in change:
        if change[time] == "L":
            cd = (cd - 1) % 4
        if change[time] == "D":
            cd = (cd + 1) % 4

    time += 1


print(time)
