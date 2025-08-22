def solution(n, w, num):
    # boxes[col] = 해당 열(스택)에 쌓인 상자 번호들 (아래→위 순서로 append 되어 끝이 '위')
    boxes = [[] for _ in range(w)]

    number = 1
    direction = 1  # 1: 왼→오, -1: 오→왼 (한 줄 채울 때마다 방향을 뒤집는 플래그)

    # 1부터 n까지 번호를 지그재그로 열에 배치
    while number <= n:
        if direction == 1:
            # 왼쪽열(0)부터 오른쪽열(w-1)까지 순서대로 쌓기
            for col in range(w):
                boxes[col].append(number)  # 해당 열의 '위'에 올림
                number += 1
                if number > n:
                    break
        else:
            # 오른쪽열(w-1)부터 왼쪽열(0)까지 역방향으로 쌓기
            for col in range(w - 1, -1, -1):
                boxes[col].append(number)
                number += 1
                if number > n:
                    break
        # 다음 라인은 반대 방향으로 진행
        direction *= -1

    # 배치가 끝났으니, num이 들어있는 열을 찾아 '위에서 몇 번째'인지 계산
    for box in boxes:
        if num in box:
            # box는 아래→위 순서로 저장되어 있으므로
            #   위에서의 위치 = len(box) - index(num)
            # 예) [1, 5, 9]에서 9는 맨 위(3 - 2 = 1번째), 5는 위에서 2번째(3 - 1 = 2)
            return len(box) - box.index(num)

    # num이 범위 밖이면 0 (문제 맥락상 거의 도달하지 않음)
    return 0
