from itertools import permutations

n = int(input())
inning = [list(map(int, input().split())) for _ in range(n)]

players = [i for i in range(1, 9)]  # 1번 선수(인덱스 0)를 제외한 선수들
max_score = 0

# 1번 선수(인덱스 0)를 4번 타자(3번째 인덱스)에 고정
for order in permutations(players, 8):
    order = list(order)
    order.insert(3, 0)

    score = 0
    current_batter = 0  # 이닝이 바뀌어도 이어져야 하므로, 이 위치에 선언

    # n이닝 진행
    for i in range(n):
        out_count = 0
        # bases: [1루, 2루, 3루]에 주자가 있는지 여부(0 or 1)
        bases = [0, 0, 0]

        # 매 이닝의 타격 결과 리스트를 변수에 담아두면 접근 속도가 빨라짐
        scores = inning[i]

        # 3아웃 될 때까지 진행
        while out_count < 3:
            # 이번 타자의 결과
            result = scores[order[current_batter]]

            if result == 0:  # 아웃
                out_count += 1
            elif result == 1:  # 안타
                # 3루 주자 홈인
                score += bases[2]
                # 주자 이동 (3루 <- 2루, 2루 <- 1루, 1루 <- 새 타자)
                bases[2] = bases[1]
                bases[1] = bases[0]
                bases[0] = 1
            elif result == 2:  # 2루타
                # 3루, 2루 주자 홈인
                score += bases[2] + bases[1]
                # 주자 이동 (3루 <- 1루, 2루 <- 새 타자)
                bases[2] = bases[0]
                bases[1] = 1
                bases[0] = 0
            elif result == 3:  # 3루타
                # 모든 주자 홈인
                score += bases[2] + bases[1] + bases[0]
                # 타자는 3루로
                bases = [0, 0, 1]
            else:  # result == 4, 홈런
                # 모든 주자 + 타자 홈인
                score += bases[2] + bases[1] + bases[0] + 1
                bases = [0, 0, 0]

            # 다음 타자
            current_batter = (current_batter + 1) % 9

    # 최대 점수 갱신
    max_score = max(max_score, score)

print(max_score)
