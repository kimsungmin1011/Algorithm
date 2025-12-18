from collections import deque

n = int(input())
k = int(input())

apple = set()

for _ in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    apple.add((x, y))

l = int(input())
change = {}

for _ in range(l):
    line = list(input().split())
    change[int(line[0])] = line[1]


def changedef(d, turn):
    if turn == "L":
        d -= 1
        if d < 0:
            d = 3
    else:
        d = (d + 1) % 4
    return d


time = 1
sx, sy = 0, 0
d = 1

snake_list = deque([(0, 0)])

while True:
    if d == 0:
        sx -= 1
    elif d == 1:
        sy += 1
    elif d == 2:
        sx += 1
    elif d == 3:
        sy -= 1

    if sx >= n or sy >= n or sx < 0 or sy < 0 or (sx, sy) in snake_list:
        break
    elif (sx, sy) in apple:
        apple.remove((sx, sy))  # 사과는 먹으면 사라짐
        snake_list.append((sx, sy))
    else:
        snake_list.append((sx, sy))
        snake_list.popleft()

    if time in change:
        turn = change[time]
        d = changedef(d, turn)

    time += 1

print(time)
