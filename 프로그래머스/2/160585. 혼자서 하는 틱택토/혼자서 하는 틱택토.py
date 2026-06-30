def solution(board):
    first = 0
    second = 0
    dx = [1, 1, 1, 0]
    dy = [-1, 1, 0, 1]

    for line in board:
        for node in line:
            if node == 'O':
                first += 1
            elif node == 'X':
                second += 1

    # 검증 1: 턴 순서 (O 선공)
    if not (first == second or first == second + 1):
        return 0

    def dfs(d, x, y):
        c = 1
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < 3 and 0 <= ny < 3 and board[x][y] == board[nx][ny]:
            c += dfs(d, nx, ny)
        return c

    # 검증 2: 승리 후 게임 진행 불가
    win = None
    for i, j in [[0, 0], [0, 1], [0, 2], [1, 0], [2, 0]]:
        if board[i][j] != '.':
            for d in range(4):
                if dfs(d, i, j) == 3:
                    if win is not None and win != board[i][j]:  # 둘 다 이김 → 불가능
                        return 0
                    win = board[i][j]

    # 이긴 사람이 마지막 수를 둔 것이어야 함
    if win == 'O' and first != second + 1:
        return 0
    if win == 'X' and first != second:
        return 0

    return 1