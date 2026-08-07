def solution(info, n, m):
    INF = float('inf')
    item_count = len(info)

    # dp[i][b] =
    # i개의 물건을 모두 처리했을 때
    # B의 누적 흔적이 정확히 b인 경우의 A 최소 누적 흔적
    #
    # 도달할 수 없는 상태는 INF로 초기화한다.
    dp = [
        [INF] * m
        for _ in range(item_count + 1)
    ]

    # 물건을 하나도 처리하지 않은 상태
    # A 흔적 = 0, B 흔적 = 0
    dp[0][0] = 0

    # 물건을 하나씩 처리한다.
    for i in range(1, item_count + 1):
        a_trace, b_trace = info[i - 1]

        # 현재 물건까지 처리했을 때 가능한
        # 모든 B의 누적 흔적을 확인한다.
        for current_b in range(m):

            # ----------------------------------------
            # 경우 1: 현재 물건을 A가 훔친다.
            # ----------------------------------------
            # B는 훔치지 않았으므로 B 흔적은 current_b 그대로다.
            #
            # dp[i - 1][current_b]
            # = 이전 물건까지 처리했을 때의 A 흔적
            next_a = dp[i - 1][current_b] + a_trace

            # A의 흔적이 n보다 작아야 잡히지 않는다.
            if next_a < n:
                dp[i][current_b] = min(dp[i][current_b], next_a)

            # ----------------------------------------
            # 경우 2: 현재 물건을 B가 훔친다.
            # ----------------------------------------
            # 현재 B 흔적이 current_b가 되려면
            # 이전 B 흔적은 current_b - b_trace여야 한다.
            previous_b = current_b - b_trace

            if (
                previous_b >= 0
                and dp[i - 1][previous_b] != INF
            ):
                # B가 현재 물건을 훔쳤으므로
                # A의 흔적은 증가하지 않는다.
                dp[i][current_b] = min(
                    dp[i][current_b],
                    dp[i - 1][previous_b]
                )

    # 모든 물건을 처리한 마지막 행에서
    # A의 흔적이 가장 작은 값을 찾는다.
    answer = min(dp[item_count])

    return answer if answer != INF else -1