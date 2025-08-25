def solution(players, m, k):
    answer = 0
    # server[i]: i시점에 '추가 임시 서버'가 몇 대나 살아있는지(기본 서버 1대는 항상 있다고 가정)
    server = [0 for _ in range(24)]

    for i in range(24):
        # 현재 시각 i의 총 처리 가능 인원 = (기본 1대 + 추가 서버 server[i]) * m
        # 비교를 (… * m) 대신 (… * m + m - 1)로 하는 이유:
        #   players[i] <= (server[i] + 1) * m - 1  <=>  players[i] < = 총용량 - 1
        #   즉, players[i]가 현재 용량 이내이면 추가 서버 불필요.
        if players[i] <= server[i] * m + m - 1:
            continue
        else:
            # 필요한 '추가 임시 서버' 개수를 count로 계산
            count = 0
            # players[i]가 (기존 추가서버 + 새로 더한 count + 기본 1대)의 용량 이내가 될 때까지 증가
            # 비교식: players[i] <= (server[i] + count) * m + m - 1
            while players[i] > (server[i] + count) * m + m - 1:
                count += 1

            # 이번 시각에 새로 연 임시 서버 수를 누적
            answer += count

            # 임시 서버는 k시간 지속 → i, i+1, ..., i+k-1 범위에 반영
            for j in range(k):
                if i + j <= 23:
                    server[i + j] += count

    return answer