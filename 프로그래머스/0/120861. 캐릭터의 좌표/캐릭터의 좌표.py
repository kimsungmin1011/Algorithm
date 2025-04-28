def solution(keyinput, board):
    x, y = 0, 0
    width, height = board[0], board[1]

    for command in keyinput:
        if command == "left":
            if y - 1 >= -(width // 2):
                y -= 1
        elif command == "right":
            if y + 1 <= width // 2:
                y += 1
        elif command == "down":
            if x - 1 >= -(height // 2):
                x -= 1
        elif command == "up":
            if x + 1 <= height // 2:
                x += 1

    answer = [y, x]

    return answer
