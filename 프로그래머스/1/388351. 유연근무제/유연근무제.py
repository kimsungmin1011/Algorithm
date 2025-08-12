def solution(schedules, timelogs, startday):
    """
    schedules[i]: 정시 도착 기준 HHMM (예: 930)
    timelogs[i]: 7일 연속 도착 HHMM 리스트 (주말 포함, 길이 7 가정)
    startday: 첫 번째 timelog의 요일 (1=월, ..., 7=일)
    규칙: 기준 시각 + 10분 이내(== 포함)면 통과, 평일(월~금)만 체크
    """
    def hhmm_to_min(hhmm):
        return (hhmm // 100) * 60 + (hhmm % 100)

    answer = 0
    for i in range(len(schedules)):
        cutoff = hhmm_to_min(schedules[i]) + 10  # 10분 허용
        ok = True

        for d in range(7):
            dow = ((startday - 1 + d) % 7) + 1  # 1~7 반복
            if dow in (6, 7):  # 토, 일 스킵
                continue

            arrive = hhmm_to_min(timelogs[i][d])
            if arrive > cutoff:  # 같은 시각은 통과, 더 늦으면 탈락
                ok = False
                break

        if ok:
            answer += 1

    return answer
