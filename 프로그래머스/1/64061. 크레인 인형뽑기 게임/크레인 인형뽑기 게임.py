def solution(board, moves):
    answer = 0
    stack = []

    for i in moves:
        current = 0

        for i2 in range(len(board)):
            if board[i2][i - 1] != 0:
                current = board[i2][i - 1]
                board[i2][i - 1] = 0
                break

        if current == 0:
            continue

        if len(stack) == 0:
            stack.append(current)
        else:
            if stack[-1] == current:
                answer += 1
                while stack and stack[-1] == current:
                    stack.pop()
                    answer += 1
            else:
                stack.append(current)

    return answer
