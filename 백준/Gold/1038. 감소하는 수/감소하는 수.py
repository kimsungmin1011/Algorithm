n = int(input())
final_answer = []

number_list = []


def dfs(idx):
    if number_list:
        final_answer.append(int("".join(number_list)))

    for i in range(idx):
        number_list.append(str(i))
        dfs(i)
        number_list.pop()


dfs(10)

if len(final_answer) >= n + 1:
    print(sorted(final_answer)[n])
else:
    print(-1)
