answer = 0


def solution(n):
    global answer
    daekaksunright = [False] * (2 * n)  # / 대각선 방문 배열 (범위: 0 ~ 2*n)
    daekaksunleft = [False] * (2 * n)  # \ 대각선 방문 배열 (범위: -n ~ n)
    yeol = [False] * n  # 열 방문 배열

    def dfs(idx):
        global answer
        if idx == n:
            answer += 1
            return

        # 행(idx)을 기준으로 이전에 탐색하던 행의 다음 행 탐색 (각 행마다 최소 한 개의 퀸이 있어야 함)
        for j in range(n):
            if (
                daekaksunleft[idx - j] == False
                and daekaksunright[idx + j] == False
                and yeol[j] == False
            ):
                daekaksunleft[idx - j] = True
                daekaksunright[idx + j] = True
                yeol[j] = True
                dfs(idx + 1)
                # 백트래킹 원복
                daekaksunleft[idx - j] = False
                daekaksunright[idx + j] = False
                yeol[j] = False

    dfs(0)

    return answer
