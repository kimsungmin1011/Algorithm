answer = 0


def solution(n):
    global answer
    daekaksunright = [False] * (2 * n)  # / 대각선 방문 배열
    daekaksunleft = [False] * (2 * n)  # \ 대각선 방문 배열
    yeol = [False] * n  # 열 방문 배열

    def dfs(idx):
        global answer
        # idx가 n과 같으면 n개의 퀸을 모두 놓은 것이므로 경우의 수 +1
        if idx == n:
            answer += 1
            return

        for j in range(n):
            if (
                not daekaksunleft[idx - j]
                and not daekaksunright[idx + j]
                and not yeol[j]
            ):
                # 퀸 놓기
                daekaksunleft[idx - j] = True
                daekaksunright[idx + j] = True
                yeol[j] = True

                dfs(idx + 1)  # 인자는 하나만!

                # 백트래킹 원복
                daekaksunleft[idx - j] = False
                daekaksunright[idx + j] = False
                yeol[j] = False

    dfs(0)
    return answer
