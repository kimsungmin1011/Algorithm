result = 0  # 경우의 수


def solution(n):
    global result

    array_y = [False] * n  # 각 행(row)에 퀸이 있는지 표시
    array_l = [False] * 2 * n  # 왼쪽 대각선(\)에 퀸이 있는지 표시
    array_r = [False] * 2 * n  # 오른쪽 대각선(/)에 퀸이 있는지 표시

    # 한 개 열씩 모든 열을 탐색하는 백트래킹 DFS
    def dfs(num):
        global result
        # (1) 기저 조건: 모든 열에 퀸을 놓았다면 해 하나 완성
        if num == n:
            result += 1
            return

        # (2) 현재 열(num)에 퀸을 놓을 수 있는 모든 행(i) 탐색
        for i in range(n):
            # 행, 왼쪽 대각, 오른쪽 대각 모두 비어 있어야 놓을 수 있음
            if not array_y[i] and not array_l[i - num] and not array_r[i + num]:
                # (3) 퀸 놓기: 표시
                array_y[i] = array_l[i - num] = array_r[i + num] = True
                # (4) 다음 열로 재귀 호출
                dfs(num + 1)
                # (5) 되돌리기(백트래킹): 표시 해제
                array_y[i] = array_l[i - num] = array_r[i + num] = False

    dfs(0)

    # 경우의 수 반환
    return result
