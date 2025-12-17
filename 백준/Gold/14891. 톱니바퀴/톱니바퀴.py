topni = []

for i in range(4):
    topni.append(list(input()))

n = int(input())
turn = []

for _ in range(n):
    turn.append(list(map(int, input().split())))

for i, d in turn:
    new_topni = topni[:]
    i -= 1

    if d == 1:
        new_topni[i] = list(topni[i][-1]) + topni[i][:-1]
    else:
        new_topni[i] = topni[i][1:] + list(topni[i][0])

    # 만약 왼쪽이 다르면
    if i - 1 >= 0 and topni[i - 1][2] != topni[i][6]:
        number = i
        nd = d * -1

        while number - 1 >= 0:
            if topni[number - 1][2] == topni[number][6]:
                # 일치하면 탐색 종료
                break
            if nd == 1:
                new_topni[number - 1] = (
                    list(topni[number - 1][-1]) + topni[number - 1][:-1]
                )
            else:
                new_topni[number - 1] = topni[number - 1][1:] + list(
                    topni[number - 1][0]
                )

            number -= 1
            nd *= -1

    # 만약 오른쪽이 다르면
    if i + 1 < 4 and topni[i][2] != topni[i + 1][6]:
        number = i
        nd = d * -1

        while number + 1 <= 3:
            if topni[number][2] == topni[number + 1][6]:
                # 일치하면 탐색 종료
                break
            if nd == 1:
                new_topni[number + 1] = (
                    list(topni[number + 1][-1]) + topni[number + 1][:-1]
                )
            else:
                new_topni[number + 1] = topni[number + 1][1:] + list(
                    topni[number + 1][0]
                )

            number += 1
            nd *= -1

    topni = new_topni[:]

count = 0

for i in range(4):
    if topni[i][0] == "1":
        count += 1 * 2**i

print(count)
