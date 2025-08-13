def solution(friends, gifts):
    # save[i][j] => i가 j에게 준 선물의 개수
    save = [[0 for _ in range(len(friends))] for _ in range(len(friends))]

    for gift in gifts:
        giver, taker = gift.split(" ")
        save[friends.index(giver)][friends.index(taker)] += 1
        save[friends.index(taker)][friends.index(giver)] -= 1

    receive = [0 for _ in range(len(friends))]

    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if save[i][j] > 0:
                receive[i] += 1
            elif save[i][j] < 0:
                receive[j] += 1
            else:
                if sum(save[i]) > sum(save[j]):
                    receive[i] += 1
                if sum(save[j]) > sum(save[i]):
                    receive[j] += 1

    return max(receive)  # 가장 많은 선물을 받는 친구가 받을 선물의 수
