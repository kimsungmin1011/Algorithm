import heapq


def solution(scoville, K):
    heapq.heapify(scoville)  # 리스트를 min heap으로 변환
    answer = 0

    while len(scoville) >= 2 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = first + second * 2
        heapq.heappush(scoville, mixed)
        answer += 1

    # 마지막 검사
    if scoville[0] >= K:
        return answer
    else:
        return -1
