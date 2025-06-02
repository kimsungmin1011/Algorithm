t = int(input())

for _ in range(t):
    n = int(input())
    answer = [0 for _ in range(5)]

    # 60분, 10분, 1분 단위로 시간 분해
    sixty, ten, one = n // 60, (n % 60) // 10, n % 10

    # 1분이 6 이상이면, 10분을 하나 더 쓰고 1분을 음수로 보정 (더 짧은 버튼 횟수)
    if one > 5:
        ten += 1
        one -= 10

    # 10분이 4 이상이면, 60분을 하나 더 쓰고 10분을 음수로 보정
    if ten > 3:
        sixty += 1
        ten -= 6

    # 예외 케이스: ten이 음수고, one이 5이면 → ten += 1, one -= 10로 보정 (버튼 횟수 줄임)
    if ten < 0 and one == 5:
        ten += 1
        one -= 10

    # 결과를 answer 배열에 분배
    answer[0] = sixty

    if ten >= 0:
        answer[1] = ten
    else:
        answer[2] = abs(ten)

    if one >= 0:
        answer[3] = one
    else:
        answer[4] = abs(one)

    print(*answer)
