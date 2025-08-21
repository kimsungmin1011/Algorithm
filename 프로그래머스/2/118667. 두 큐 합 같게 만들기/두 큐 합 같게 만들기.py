from collections import deque


def solution(queue1, queue2):
    answer = -2

    len_q1 = len(queue1)
    len_q2 = len(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    q1 = deque(queue1)
    q2 = deque(queue2)

    count = 0
    while True:

        # 적당히 돌려보다가 안되면 -1리턴
        if count > (len_q1 + len_q2) * 2:
            return -1

        # 두 큐의 합이 같아지면 그만
        if sum1 == sum2:
            answer = count
            break

        # 큐2의 sum이 더 크면 큐2에서 뽑아서 q1에 넣음
        if q2 and sum1 < sum2:
            elem2 = q2.popleft()
            q1.append(elem2)

            sum1 += elem2
            sum2 -= elem2

        # 반대면 반대로
        elif q1 and sum1 >= sum2:
            elem1 = q1.popleft()
            q2.append(elem1)

            sum1 -= elem1
            sum2 += elem1

        count += 1

    return answer
