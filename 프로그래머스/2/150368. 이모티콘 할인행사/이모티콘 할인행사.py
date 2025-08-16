array = []
discount = [0.1, 0.2, 0.3, 0.4]


def dfs(d_list, l, index):
    if index == l:
        d_list.append(array[:])
        return

    for i in range(4):
        array.append(discount[i])
        dfs(d_list, l, index + 1)
        array.pop()


def solution(users, emoticons):
    answer = []
    d_list = []  # 모든 할인비율 집합 리스트
    dfs(d_list, len(emoticons), 0)

    for i in range(len(d_list)):
        c_discount = d_list[i]
        t_member, t_cost = 0, 0
        for cut, cost in users:
            c_cost = 0
            for k in range(len(emoticons)):
                if c_discount[k] * 100 >= cut:
                    c_cost += emoticons[k] * (1 - c_discount[k])
            if c_cost >= cost:
                t_member += 1
            else:
                t_cost += c_cost
        answer.append((t_member, t_cost))

    return sorted(answer, reverse=True)[0]
