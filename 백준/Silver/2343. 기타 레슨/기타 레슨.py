n, m = map(int, input().split())
lessons = list(map(int, input().split()))

start = max(lessons)
end = sum(lessons)

while start <= end:
    mid = (start + end) // 2  # 가능한 블루레이 크기 중 최소
    count = 1  # 필요한 블루레이 개수
    current_time = 0  # 현재 블루레이의 시간

    for lesson in lessons:
        if current_time + lesson > mid:
            count += 1
            current_time = lesson
        else:
            current_time += lesson

    if count > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)
