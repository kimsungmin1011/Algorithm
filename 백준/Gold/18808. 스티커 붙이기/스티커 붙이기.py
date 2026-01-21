n, m, k = map(int, input().split())
paper = [[0 for _ in range(m)] for _ in range(n)]


def check(x, y, current):
    for i in range(n - x + 1):  # 종이에서 스티커 좌상단 row
        for j in range(m - y + 1):  # 종이에서 스티커 좌상단 col
            ok = True

            # 1) 충돌 검사
            for sr in range(x):  # 스티커 row
                for sc in range(y):  # 스티커 col
                    if current[sr][sc] == 1 and paper[i + sr][j + sc] != 0:
                        ok = False
                        break
                if not ok:
                    break

            # 2) 붙이기
            if ok:
                for sr in range(x):
                    for sc in range(y):
                        if current[sr][sc] == 1:
                            paper[i + sr][j + sc] = 1
                return True

    return False


# 90도 시계 방향 회전
def turn():
    global current, r, c
    rotated = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            rotated[j][r - 1 - i] = current[i][j]

    current = rotated
    r, c = c, r


for _ in range(k):
    current = []
    r, c = map(int, input().split())
    for _ in range(r):
        current.append(list(map(int, input().split())))

    count = 0
    while True:
        if count == 4:
            break
        if check(r, c, current) == False:
            turn()
            count += 1
        else:
            break

count = 0

for i in range(n):
    for j in range(m):
        if paper[i][j] != 0:
            count += 1

print(count)
