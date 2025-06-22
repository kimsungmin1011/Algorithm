max_score_diff = -int(1e9)  # 최대 점수 차이
answer = []


def solution(n, info):
    global max_score_diff, answer
    lion_record = [0 for _ in range(11)]

    def dfs(idx, lion_score, remains):
        # 현재 점수 번호, 라이언 점수, 라이언 화살 개수, 라이언 과녁별 화살, 어피치 과녁별 화살
        global max_score_diff, answer

        # 끝까지 다 탐색하면 종료
        if idx == 10:
            # 화살 남았으면 0점에 다 넣음
            if remains > 0:
                lion_record[10] += remains

            apeach_score = 0
            for i in range(10):
                if info[i] > lion_record[i]:
                    apeach_score += 10 - i
            diff_score = lion_score - apeach_score  # 라이언과 어피치의 점수 차이
            # 라이언이 더 많이 득점했다면
            if diff_score > 0:
                if diff_score == max_score_diff:
                    # 점수 차이가 같다면
                    answer.append(lion_record[:])
                elif diff_score > max_score_diff:
                    # 점수 차이가 더 크다면
                    max_score_diff = diff_score
                    answer = [lion_record[:]]

            # 원복
            if remains > 0:
                lion_record[10] -= remains
            return

        apeach_count = info[idx]  # 현재 과녁에서 어치피가 맞힌 화살 개수

        # 만약 남아있는 화살로 어피치보다 더 많이 맞힐 수 있다면
        if remains > apeach_count:
            # 현재 점수에 어피치보다 한발 더 투자
            lion_record[idx] = apeach_count + 1
            dfs(idx + 1, lion_score + (10 - idx), remains - (apeach_count + 1))
            # 백트래킹 원복
            lion_record[idx] = 0

        # 현재 점수 포기하고 다음 점수로 이동
        dfs(idx + 1, lion_score, remains)

    dfs(0, 0, n)

    if answer:
        answer.sort(key=lambda x: x[::-1], reverse=True)
        return answer[0]
    else:
        return [-1]
