from itertools import combinations


def solution(orders, course):
    answer = []
    alphabet = set()

    for i in orders:
        for j in i:
            alphabet.add(j)

    # 음식 개수에 따라 조합 변경
    for length in course:
        # 현재 음식 개수에 따른 모든 코스 조합
        food_combi = list(combinations(list(alphabet), length))

        course_can = {}  # 손님들 주문 횟수 카운트

        for i in food_combi:
            course_can["".join(i)] = 0

        for customer in orders:
            customer = set(customer)
            for i in food_combi:
                flag = True
                for j in i:
                    if j not in customer:
                        flag = False
                        break
                if flag == True:
                    course_can["".join(i)] += 1

        max_value = max(course_can.values())
        if max_value <= 1:
            break

        for i in course_can:
            if course_can["".join(i)] == max_value:
                answer.append("".join(sorted(i)))
                # print("".join(sorted(i)))

    return sorted(answer)
