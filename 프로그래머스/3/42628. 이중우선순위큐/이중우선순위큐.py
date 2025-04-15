import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    visited = dict()  # key: 고유 ID, value: 유효 여부
    idx = 0  # 고유 ID

    for op in operations:
        cmd, val = op.split()
        val = int(val)

        if cmd == "I":
            heapq.heappush(min_heap, (val, idx))
            heapq.heappush(max_heap, (-val, idx))
            visited[idx] = True
            idx += 1

        elif cmd == "D":
            if val == 1:
                # 최대값 제거
                while max_heap and not visited.get(max_heap[0][1], False):
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            elif val == -1:
                # 최소값 제거
                while min_heap and not visited.get(min_heap[0][1], False):
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    # 동기화: 아직 유효한 원소만 찾기
    while min_heap and not visited.get(min_heap[0][1], False):
        heapq.heappop(min_heap)
    while max_heap and not visited.get(max_heap[0][1], False):
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        return [0, 0]

    return [-max_heap[0][0], min_heap[0][0]]
