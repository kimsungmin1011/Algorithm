n = int(input())
alist = list(map(int, input().split()))
cal = list(map(int, input().split()))

big_value = -int(1e9)
min_value = int(1e9)


def dfs(idx, number):
    global min_value, big_value
    flag = True
    for i in cal:
        if i != 0:
            flag = False
            break

    if flag == True:
        big_value = max(big_value, number)
        min_value = min(min_value, number)
        return

    for i in range(4):
        if cal[i] > 0:
            cal[i] -= 1
            if i == 0:
                dfs(idx + 1, number + alist[idx])
            elif i == 1:
                dfs(idx + 1, number - alist[idx])
            elif i == 2:
                dfs(idx + 1, number * alist[idx])
            elif i == 3:
                if number >= 0:
                    dfs(idx + 1, number // alist[idx])
                else:
                    dfs(idx + 1, -(-number // alist[idx]))
            cal[i] += 1


dfs(1, alist[0])

print(big_value)
print(min_value)
