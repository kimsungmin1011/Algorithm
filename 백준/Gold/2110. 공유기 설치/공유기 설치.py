n, c = map(int, input().split())
location = [int(input()) for _ in range(n)]
location.sort()

start = 1
end = location[-1] - location[0]
answer = 0

while start <= end:
    mid = (start + end) // 2  # 공유기 사이의 최소 거리 후보

    count = 1  # 첫 집에 공유기 하나 설치
    last_pos = location[0]  # 마지막으로 설치한 집 위치

    for i in range(1, n):
        # last_pos와 현재 위치의 거리가 mid 이상이면 설치
        if location[i] - last_pos >= mid:
            count += 1
            last_pos = location[i]

    # mid 거리로 공유기 c개 이상 설치 가능 ⇒ 현재 mid를 정답 후보에 저장
    if count >= c:
        # 더 큰 최소 거리도 가능한지 탐색하기 위해 시작점을 mid+1로 이동
        answer = mid
        start = mid + 1
    else:
        # 설치 개수가 부족 ⇒ 최소 거리를 줄여서 가능한지 탐색하기 위해 끝점을 mid-1로 이동
        end = mid - 1


print(answer)
