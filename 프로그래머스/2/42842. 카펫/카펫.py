# 주어진 갈색(brown)과 노란색(yellow) 격자의 수를 이용해 카펫의 가로, 세로 크기를 구하는 함수
def solution(brown, yellow):
    answer = []
    # 카펫의 가로 + 세로 값 (가로는 세로 이상)
    # 공식 유도: 전체 둘레 = brown + 4, 따라서 (가로 + 세로) = (brown + 4) // 2
    karosaero_sum = (brown + 4) // 2
    # 가능한 가로, 세로 쌍 후보 저장
    karosaero_candidate = []

    # 가능한 가로와 세로 쌍을 찾기 위한 반복문
    for i in range(1, karosaero_sum):
        # 조건: 가로(x)가 세로(y)보다 크거나 같아야 함
        if i >= karosaero_sum - i:
            # 가로(x), 세로(y) 후보 추가
            karosaero_candidate.append((i, karosaero_sum - i))

    # 모든 후보 쌍에 대해 유효한 조합인지 확인
    for x, y in karosaero_candidate:
        # 조건: 전체 넓이에서 brown과 yellow를 뺀 값이 0이면 조건에 부합
        # 즉, 전체 넓이 == brown + yellow
        if x * y - brown - yellow == 0:
            # 정답: 조건을 만족하는 가로, 세로 쌍 저장
            answer = [x, y]
            break

    return answer
