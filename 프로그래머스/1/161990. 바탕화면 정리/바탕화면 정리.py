def solution(wallpaper):
    answer = []
    start_x, start_y, end_x, end_y = int(1e9), int(1e9), 0, 0

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                start_x, start_y = min(i, start_x), min(j, start_y)
                end_x, end_y = max(i, end_x), max(j, end_y)

    answer = [start_x, start_y, end_x + 1, end_y + 1]

    return answer
