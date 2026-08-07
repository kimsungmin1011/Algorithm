from math import sqrt


def solution(r1, r2):
    # x >= 0, y > 0인 한쪽 영역의 점 개수
    quar = 0
    
    # x**2 + y**2 = r**2 => y**2 = r**2 - x**2
    # x < r1인 구간은 세로줄이 작은 원을 통과한다.
    for x in range(0, r1):
        quar += (
            # 큰 원 안에 있는 양의 정수 y의 개수
            int(sqrt(r2**2 - x**2))

            # 작은 원 내부에 있는 양의 정수 y의 개수
            # 작은 원의 경계는 포함해야 하므로 -1을 사용한다.
            - int(sqrt(r1**2 - x**2 - 1))
        )

    # x >= r1이면 이미 작은 원의 경계 또는 바깥이므로
    # 작은 원 내부의 점을 빼지 않아도 된다.
    for x in range(r1, r2):

        # 큰 원 안에 있는 양의 정수 y의 개수
        quar += int(sqrt(r2**2 - x**2))

    # 원이 상하좌우로 대칭이므로 4배
    return quar * 4