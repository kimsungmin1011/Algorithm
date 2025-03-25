from collections import deque

def solution(bridge_length, weight, truck_weights):
    length = len(truck_weights)  # 초기 트럭 대수
    answer = 0  # 모든 트럭이 다리를 지날 때까지 걸리는 시간
    bridge = [0 for _ in range(bridge_length)]
    truck_weights = deque(truck_weights)
    count = 0  # 다리에 있는 트럭 대수
    bye = 0  # 다리 건넌 트럭 대수

    while True:
        answer += 1

        # 다리 끝단에 트럭 있으면 곧 건널 예정
        if bridge[0] > 0:
            count -= 1
            bye += 1

        # 다리에서 트럭 한 칸씩 이동
        for i in range(bridge_length - 1):
            bridge[i] = bridge[i + 1]

        bridge[-1] = 0  # 오른쪽 끝에 있는 트럭 초기화

        # 모든 트럭이 다 건넜다면
        if bye == length:
            return answer

        if (
            truck_weights  # 아직 건너지 않은 트럭이 남아있음
            and count + 1 <= bridge_length  # 다리에 올라갈 수 있는 트럭 수
            and sum(bridge) + truck_weights[0] <= weight  # 다리가 견딜 수 있는 무게
        ):
            count += 1
            bridge[-1] = truck_weights[0]
            truck_weights.popleft()

# 입력 처리
n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

# 함수 호출 및 출력
print(solution(w, L, trucks))
