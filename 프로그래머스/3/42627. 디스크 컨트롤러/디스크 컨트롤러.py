import heapq


def solution(jobs):
    jobs.sort()
    waiting = []  # 대기작업 우선순위 큐
    answer = 0  # 작업 요청부터 종료까지 걸린 시간의 총합
    idx = 0  # 현재 추가한 작업 번호
    current = 0  # 현재시간
    count = 0  # 완료한 작업 개수

    while count <= len(jobs):
        # 1. 현재 시간 이전에 입력된 애들 다 넣어
        while idx < len(jobs) and current >= jobs[idx][0]:
            # 우선순위 소요시간 - 요청시간 순서
            heapq.heappush(waiting, (jobs[idx][1], jobs[idx][0]))
            idx += 1  # 다음 작업으로

        # 2. 만약 대기 중인 작업이 있다면
        if waiting:
            # 현재 작업 소요시간, 시작시간, 번호
            length, start = heapq.heappop(waiting)
            current = max(current, start) + length  # 이 작업의 종료시간으로
            answer += current - start  # 작업 요청부터 종료까지 걸린 시간
            count += 1
        # 3. 대기 중인 작업이 없다면 가장 가까운 작업 요청 시간으로 이동
        else:
            current = jobs[idx][0]

        # 모든 작업을 다 수행했다면 종료
        if count == len(jobs):
            break

    return answer // len(jobs)