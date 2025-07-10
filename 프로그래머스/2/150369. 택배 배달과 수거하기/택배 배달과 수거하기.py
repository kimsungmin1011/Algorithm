def solution(cap, n, deliveries, pickups):
    """
    모든 배달과 수거를 완료하는 데 필요한 최소 총 이동 거리를 계산하는 함수입니다.

    매개변수:
    cap (int): 트럭의 최대 적재 및 수거 용량입니다.
    n (int): 위치(집)의 개수입니다.
    deliveries (list of int): 각 위치별 배달해야 할 물품 개수입니다.
    pickups (list of int): 각 위치별 수거해야 할 물품 개수입니다.

    반환값:
    int: 모든 배달과 수거를 완료하는 데 이동한 총 거리입니다.
    """
    answer = 0  # 이동한 총 거리를 누적합니다
    di = n - 1  # 아직 배달이 남은 가장 먼 위치를 가리키는 포인터
    pi = n - 1  # 아직 수거가 남은 가장 먼 위치를 가리키는 포인터

    # 모든 배달과 수거가 완료될 때까지 반복합니다
    while di >= 0 or pi >= 0:
        # 배달이 남아있는 다음 위치를 찾기 위해 di 포인터를 뒤로 이동합니다
        # 이미 배달이 완료된 위치는 건너뜁니다
        while di >= 0 and deliveries[di] == 0:
            di -= 1
        # 수거가 남아있는 다음 위치를 찾기 위해 pi 포인터를 뒤로 이동합니다
        # 이미 수거가 완료된 위치는 건너뜁니다
        while pi >= 0 and pickups[pi] == 0:
            pi -= 1

        # 두 포인터가 모두 범위를 벗어나면 모든 배달과 수거가 완료된 것입니다
        if di < 0 and pi < 0:
            break

        # 배달 또는 수거가 필요한 가장 먼 위치를 결정합니다
        # 위치는 0부터 시작하므로 +1을 해주고, 왕복이므로 2를 곱합니다
        distance = max(di, pi) + 1
        answer += distance * 2

        # 이번 왕복에서 배달을 처리합니다
        load = cap  # 현재 배달 가능한 용량
        while di >= 0 and load > 0:
            if deliveries[di] <= load:
                # 해당 위치의 모든 물품을 배달하고 포인터를 뒤로 이동합니다
                load -= deliveries[di]
                deliveries[di] = 0
                di -= 1
            else:
                # 가능한 만큼만 배달하고 남은 물품 개수를 갱신합니다
                deliveries[di] -= load
                load = 0

        # 이번 왕복에서 수거를 처리합니다
        free_space = cap  # 현재 수거 가능한 용량
        while pi >= 0 and free_space > 0:
            if pickups[pi] <= free_space:
                # 해당 위치의 모든 물품을 수거하고 포인터를 뒤로 이동합니다
                free_space -= pickups[pi]
                pickups[pi] = 0
                pi -= 1
            else:
                # 가능한 만큼만 수거하고 남은 물품 개수를 갱신합니다
                pickups[pi] -= free_space
                free_space = 0

    # 모든 배달과 수거를 완료한 후 누적된 총 왕복 거리를 반환합니다
    return answer
