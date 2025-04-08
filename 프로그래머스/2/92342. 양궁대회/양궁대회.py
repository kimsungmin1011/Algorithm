import copy

answer = []
max_score = -int(1e9)


def solution(n, info):
    global max_score, answer
    answer = []
    max_score = -int(1e9)

    # score: key는 점수(10~0), value는 어피치가 해당 점수에 쏜 화살 수
    # (인덱스 0: 10점, 인덱스 10: 0점)
    score = {}
    for i in range(10, -1, -1):
        score[i] = info[10 - i]

    # helper 함수: 현재 라이언의 배분(current)과 info를 바탕으로
    # (라이언 점수 - 어피치 점수)를 계산.
    # 각 구간(점수 s)에 대해, 현재 배분 current[10-s]가
    # 어피치의 배분 info[10-s]보다 많으면 라이언이 s점 획득,
    # 그렇지 않고 어피치가 한 번 이상 쏜 경우 어피치가 s점 획득합니다.
    def calc_diff(current):
        ryan_score = 0
        apeach_score = 0
        for s in range(10, -1, -1):
            idx = 10 - s  # current의 인덱스 매핑
            if current[idx] > info[idx]:
                ryan_score += s
            elif info[idx] > 0:
                apeach_score += s
        return ryan_score - apeach_score

    def dfs(left, point, current):
        global max_score, answer
        # 화살을 다 사용한 경우: 현재 배분을 기반으로 최종 점수 차 계산
        if left == 0:
            diff = calc_diff(current)
            if diff > 0:  # 라이언이 이긴 경우에만 후보로 고려
                if diff > max_score:
                    max_score = diff
                    answer = [current[:]]
                elif diff == max_score:
                    answer.append(current[:])
            return

        # 아직 처리되지 않은 각 점수대에 대해 라이언이 승리 가능한 경우 시도
        for i in range(10, -1, -1):
            if score[i] >= 0:  # 아직 해당 구간이 처리되지 않았다면
                # 해당 구간에서 라이언이 승리하려면 어피치가 쏜 화살보다 1발 더 필요
                if left >= score[i] + 1:
                    apeach_num = score[i]  # 어피치가 해당 구간에 쏜 화살 수
                    left -= (apeach_num + 1)
                    point += i  # (참고: 진행 중 점수 계산, 최종은 calc_diff 사용)
                    current[10 - i] = apeach_num + 1  # 해당 점수대에 라이언이 쏜 화살 수 기록
                    score[i] = -1  # 해당 구간은 처리됨을 표시
                    dfs(left, point, current)
                    # 백트래킹: 원상복구
                    left += (apeach_num + 1)
                    point -= i
                    current[10 - i] = 0
                    score[i] = apeach_num

        # 만약 남은 화살이 있지만 더 이상 승리할 수 있는 구간 선택이 없으면,
        # 남은 화살을 0점 구간(인덱스 10)에 모두 배정한 후 최종 점수 차 계산
        if left > 0:
            current[10] += left
            diff = calc_diff(current)
            if diff > 0:
                if diff > max_score:
                    max_score = diff
                    answer = [current[:]]
                elif diff == max_score:
                    answer.append(current[:])
            current[10] -= left  # 다시 원상복구
        return

    dfs(n, 0, [0 for _ in range(11)])

    if len(answer) == 0:
        return [-1]
    else:
        # 여러 후보가 있을 경우, 문제 조건에 따라 낮은 점수(배열의 후반부)에
        # 더 많은 화살이 배분된 경우를 우선하도록 (배열을 뒤집어 정렬하여)
        # 마지막 후보를 선택
        return sorted(answer, key=lambda x: x[::-1])[-1]
