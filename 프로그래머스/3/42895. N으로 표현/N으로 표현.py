def solution(N, number):
    # check: 이미 만들어진 수들을 저장하는 집합 (중복 방지용)
    # dic[i]: 숫자 N을 i개 사용해서 만들 수 있는 수들의 리스트
    check, dic = set(), dict()

    # 숫자 N을 i번 반복해서 만든 숫자를 먼저 초기화 (ex. N=5 -> 5, 55, 555, ...)
    for i in range(1, 9):  # N을 최대 8번까지 사용
        num = int(str(N) * i)
        if num == number:  # 바로 만들 수 있다면 최소 사용 횟수 return
            return i
        dic[i] = [num]  # i개로 만들 수 있는 숫자에 추가
        check.add(num)

    check.add(0)  # 나눗셈 처리 중 0으로 나누는 것 방지용

    # 숫자 N을 i번 사용해서 만들 수 있는 모든 조합 계산
    for i in range(2, 9):  # N을 2번부터 8번까지 사용하는 경우
        for j in range(1, i):  # j + k = i가 되도록 분할
            k = i - j
            for num_j in dic[j]:  # j개로 만든 수
                for num_k in dic[k]:  # k개로 만든 수
                    # 가능한 연산 조합
                    candidates = [
                        num_j + num_k,
                        abs(num_j - num_k),
                        num_j * num_k
                    ]
                    # 나눗셈은 0으로 나누지 않도록 예외 처리
                    if num_k != 0:
                        candidates.append(num_j // num_k)
                    if num_j != 0:
                        candidates.append(num_k // num_j)

                    for candidate in candidates:
                        if candidate in check:
                            continue
                        elif candidate == number:  # 정답이면 바로 반환
                            return i
                        dic[i].append(candidate)  # i개로 만들 수 있는 수에 추가
                        check.add(candidate)

    return -1  # 8번까지 써도 못 만들면 -1 반환