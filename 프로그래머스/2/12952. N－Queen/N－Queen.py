answer = 0


def solution(n):
    global answer
    daekaksunright = [False] * (2 * n)  # 인덱스: x + y (범위: 0 ~ 2*n 대각선 방문 배열)
    daekaksunleft = [False] * (2 * n)  # 인덱스: x - y (범위: -n ~ n 대각선 방문 배열)
    karojiksun = [False] * n  # 인덱스: x (행 방문 배열)
    saerojiksun = [False] * n  # 인덱스: y (열 방문 배열)

    def dfs(idx, count):
        global answer
        if count == n:
            answer += 1
            return

        # 행을 기준으로 이전에 탐색하던 행의 다음 행부터 탐색 (각 행마다 최소 한 개의 퀸이 있어야 함)
        for j in range(n):
            if (
                daekaksunleft[idx - j] == False
                and daekaksunright[idx + j] == False
                and karojiksun[idx] == False
                and saerojiksun[j] == False
            ):
                daekaksunleft[idx - j] = True
                daekaksunright[idx + j] = True
                karojiksun[idx] = True
                saerojiksun[j] = True
                dfs(idx + 1, count + 1)
                # 백트래킹 원복
                daekaksunleft[idx - j] = False
                daekaksunright[idx + j] = False
                karojiksun[idx] = False
                saerojiksun[j] = False

    dfs(0, 0)

    return answer
