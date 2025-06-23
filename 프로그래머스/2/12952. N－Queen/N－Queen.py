answer = 0  # 가능한 N-Queen 배치 경우의 수를 저장할 전역 변수


def solution(n):
    global answer

    # / 방향 대각선 체크 배열 (인덱스: row + col)
    daekaksunright = [False] * (2 * n)
    # \ 방향 대각선 체크 배열 (인덱스: row - col + n)
    daekaksunleft = [False] * (2 * n)
    # 열(세로 방향) 체크 배열 (인덱스: 열 번호)
    yeol = [False] * n

    def dfs(idx):
        global answer
        # 모든 행에 퀸을 하나씩 배치한 경우 → 유효한 경우의 수 +1
        if idx == n:
            answer += 1
            return

        # 현재 행(idx)에 대해 모든 열(j)을 탐색
        # N-Queen 문제의 핵심 조건: 각 행에는 반드시 퀸을 하나만 놓아야 하므로,
        # 각 재귀 호출은 해당 행에 퀸을 하나 놓는 시도를 의미함
        for j in range(n):
            # 퀸이 현재 위치 (idx, j)에 놓일 수 있는지 확인
            if (
                daekaksunleft[idx - j] == False  # \ 대각선 사용 중인지 체크
                and daekaksunright[idx + j] == False  # / 대각선 사용 중인지 체크
                and yeol[j] == False  # 열 사용 중인지 체크
            ):
                # 현재 위치에 퀸을 놓았다고 표시
                daekaksunleft[idx - j] = True
                daekaksunright[idx + j] = True
                yeol[j] = True

                # 다음 행으로 재귀 탐색
                dfs(idx + 1)

                # 백트래킹 원복
                daekaksunleft[idx - j] = False
                daekaksunright[idx + j] = False
                yeol[j] = False

    # 0번 행부터 시작
    dfs(0)

    # 가능한 경우의 수 반환
    return answer
