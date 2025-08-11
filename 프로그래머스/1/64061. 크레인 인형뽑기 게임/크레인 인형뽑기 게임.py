def solution(board, moves):
    answer = 0
    stack = []

    for i in moves:
        number = -1
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                number = board[j][i - 1]
                board[j][i - 1] = 0
                break

        if number == -1:
            continue

        if stack and number == stack[-1]:
            stack.pop()
            answer += 2
        else:
            stack.append(number)

    return answer
