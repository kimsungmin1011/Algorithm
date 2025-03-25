from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    time = 0
    total_weight = 0

    while bridge:
        time += 1
        total_weight -= bridge.popleft()  # 다리에서 트럭 한 칸 이동 (혹은 나감)

        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)  # 트럭이 못 올라감, 빈칸 유지

    return time
