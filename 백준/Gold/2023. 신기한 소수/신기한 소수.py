n = int(input())

arr = []


def dfs(c):
    if c == n:
        print("".join(arr))
        return

    for i in range(1, 10):
        arr.append(str(i))
        number = int("".join(arr))

        flag = True
        for j in range(2, int(number**0.5 + 1)):
            if number % j == 0:
                flag = False
                break
        if flag == True:
            dfs(c + 1)

        arr.pop()


for i in [2, 3, 5, 7]:
    arr.append(str(i))
    dfs(1)
    arr.pop()
