import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    min_set = set()  # 최소 힙에 아직 남아 있다고 보는 값들
    max_set = set()  # 최대 힙에 아직 남아 있다고 보는 값들
    idx = 0  # 중복 값을 구분하기 위한 번호

    for op in operations:
        cmd, val = op.split()
        val = int(val)

        if cmd == "I":
            # 같은 숫자가 여러 번 들어올 수 있으므로 (값, 번호) 형태로 저장한다.
            item = (val, idx)
            heapq.heappush(min_heap, item)
            heapq.heappush(max_heap, (-val, idx))
            min_set.add(item)
            max_set.add(item)
            idx += 1

        elif cmd == "D":
            if val == 1:
                # 최소 힙 쪽에서 이미 삭제된 값은 최대 힙에서도 건너뛴다.
                while max_heap and (-max_heap[0][0], max_heap[0][1]) not in min_set:
                    heapq.heappop(max_heap)

                if max_heap:
                    # 최대 힙 쪽에서만 제거하고, 최소 힙과의 동기화는 마지막에 한다.
                    removed = heapq.heappop(max_heap)
                    max_set.remove((-removed[0], removed[1]))

            elif val == -1:
                # 최대 힙 쪽에서 이미 삭제된 값은 최소 힙에서도 건너뛴다.
                while min_heap and min_heap[0] not in max_set:
                    heapq.heappop(min_heap)

                if min_heap:
                    # 최소 힙 쪽에서만 제거하고, 최대 힙과의 동기화는 마지막에 한다.
                    removed = heapq.heappop(min_heap)
                    min_set.remove(removed)

    # 마지막 동기화: 양쪽 set에 모두 존재하는 값만 실제로 남은 값이다.
    while max_heap and (-max_heap[0][0], max_heap[0][1]) not in min_set:
        heapq.heappop(max_heap)
    while min_heap and min_heap[0] not in max_set:
        heapq.heappop(min_heap)

    if not min_heap or not max_heap:
        return [0, 0]

    return [-max_heap[0][0], min_heap[0][0]]
