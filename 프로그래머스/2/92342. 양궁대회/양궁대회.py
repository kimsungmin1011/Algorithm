import copy

answer = []
max_score = -int(1e9)


def solution(n, info):
    global max_score, answer

    score = {}  # 각 점수별 어피치가 맞힌 화살 개수
    for i in range(10, -1, -1):
        score[i] = info[10 - i]  # (인덱스 0: 10점, 10: 0점)

    def dfs(left, point, current):
        global max_score, answer
        # 화살을 모두 사용한 경우 (기존 조건)
        if left == 0:
            apeach_score = 0
            for i in score:
                if score[i] > 0:  # 아직 어피치가 남긴 화살이 있다면
                    apeach_score += i
            diff = point - apeach_score  # 라이언과 어피치의 점수 차이
            if diff > 0:
                if diff > max_score:
                    max_score = diff
                    answer = [current[:]]
                elif diff == max_score:
                    answer.append(current[:])
            return

        # 각 점수대별로 라이언이 어피치를 이길 수 있도록 화살 배분 시도
        for i in range(10, -1, -1):
            if score[i] >= 0:  # 아직 처리되지 않은 점수대라면
                if left >= score[i] + 1:  # 어피치보다 1발 더 쏠 수 있다면
                    apeach_num = copy.deepcopy(score[i])
                    left -= apeach_num + 1  # 해당 점수대를 이기는데 필요한 화살 사용
                    point += i  # 해당 점수 획득
                    current[10 - i] = apeach_num + 1  # 라이언의 화살 배분 기록
                    score[i] = -1  # 해당 점수대는 이미 처리됨을 표시
                    dfs(left, point, current)
                    # 백트래킹: 원상복구
                    left += apeach_num + 1
                    point -= i
                    current[10 - i] = 0
                    score[i] = apeach_num

        # **추가된 부분**
        # 만약 남은 화살이 있는데 어떠한 점수대를 더 이길 수 없는 경우,
        # 남은 화살을 0점(인덱스 10)에 모두 할당하여 최종 결과를 계산
        if left > 0:
            current[10] += left  # 남은 화살 모두 0점 영역에 배정
            apeach_score = 0
            for i in score:
                if score[i] > 0:
                    apeach_score += i
            diff = point - apeach_score
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
        return sorted(answer, key=lambda x: x[::-1])[-1]
