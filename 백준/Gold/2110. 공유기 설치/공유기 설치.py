n, c = map(int, input().split())
location = [int(input()) for _ in range(n)]
location.sort()

start = 1
end = location[-1] - location[0]
answer = 0

while start <= end:
    mid = (start + end) // 2  # 시도할 “공유기 최소 거리”

    # 그리디 설치
    count = 1  # 첫 집에 무조건 설치
    last = location[0]  # 마지막에 공유기 설치한 위치
    for pos in location[1:]:
        if pos - last >= mid:
            count += 1
            last = pos

    if count >= c:
        # mid 거리로 c개 이상 설치 가능 ⇒ 더 큰 거리 시도
        answer = mid
        start = mid + 1
    else:
        # 설치 개수가 부족 ⇒ 거리를 줄여야 함
        end = mid - 1

print(answer)
