x, y = map(int, input().split())

left, right = 0, 1000000000
answer = -1
z = y * 100 // x  # 기존 승률 (정수연산)

while left <= right:
    mid = (left + right) // 2  # 추가로 플레이하는 판수
    new = (mid + y) * 100 // (mid + x)  # 새 승률 (정수연산)

    if new > z:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
