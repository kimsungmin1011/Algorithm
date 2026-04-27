import heapq


def solution(jobs):
    answer = 0
    queue = []

    ct = 0  # 현재 시간
    count = 0
    length = len(jobs)

    while count < length:
        new_jobs = []  # 남은 작업 리스트
        for i in range(len(jobs)):
            s, l = jobs[i][0], jobs[i][1]  # 요청시간, 작업시간
            if ct >= s:  # 현재 시간이 요청 시간 이후라면 추가
                heapq.heappush(queue, (l, s, i))
            else:  # 아니라면 남은 작업 리스트에 추가
                new_jobs.append((s, l))
        jobs = new_jobs[:]  # 작업 리스트 업데이트

        # 현재 디스크 컨트롤러에 작업이 있다면
        if queue:
            wt, st, ti = heapq.heappop(queue)  # 작업시간, 요청시간, 작업번호
            # 현재 시간이 요청 시간 이후라면
            if ct >= st:
                ct += wt  # 현재 시간 += 작업시간
            # 현재 시간이 요청 시간 이전이라면
            else:
                ct = st + wt  # 현재 시간 = 현재 작업 시작 시간 + 작업 시간

            answer += ct - st  # 작업 종료 시간 - 작업 요청 시간
            count += 1
        # 디스크 컨트롤러에 작업이 없다면 현재 시간을 가장 가까운 작업 요청 시간으로
        else:
            ct = min(i[0] for i in jobs)

    return answer // length
