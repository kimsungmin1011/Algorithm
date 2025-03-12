def solution(n, stations, w):
    answer = 0
    last_covered = 0  # 마지막으로 커버된 아파트 번호
    coverage = 2 * w + 1  # 하나의 기지국이 커버할 수 있는 범위

    for station in stations:
        left = station - w  # 기지국의 왼쪽 끝
        if left > last_covered + 1:  # 빈 구간이 존재하는 경우
            gap = left - (last_covered + 1)  # 빈 구간 길이
            answer += (gap + coverage - 1) // coverage  # 올림 연산으로 필요한 기지국 개수 계산
        last_covered = station + w  # 현재 기지국이 커버한 마지막 아파트

    # 마지막 기지국 이후 남은 빈 구간 처리
    if last_covered < n:
        gap = n - last_covered
        answer += (gap + coverage - 1) // coverage

    return answer
