n = int(input())

number = []
answer = 0

flag2 = False


def dfs(idx):
    global flag2, answer

    if flag2 == True:
        return

    if idx == n:
        answer = int("".join(number))
        flag2 = True
        return

    for i in range(1, 4):
        number.append(str(i))
        l = len(number) - 1
        flag = True

        for j in range(len(number) // 2):
            if number[l - 2 * j - 1 : l - j] == number[l - j :]:
                flag = False
                break

        if flag == True:
            dfs(idx + 1)

        number.pop()


dfs(0)

print(answer)
