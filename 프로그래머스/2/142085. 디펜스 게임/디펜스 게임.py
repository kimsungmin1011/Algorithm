import heapq


def solution(n, k, enemy):
    removes = []  # 무적권을 사용할 라운드의 적 수를 담는 최소 힙

    for i in range(len(enemy)):
        if len(removes) < k:
            # 무적권 여유 있음 → 현재 라운드에 무적권 사용
            heapq.heappush(removes, enemy[i])
        elif enemy[i] > removes[0]:
            # 현재 적 수 > 힙 최솟값 → 더 이득: 최솟값 라운드는 싸우고, 현재 라운드에 무적권 교체
            n -= heapq.heappop(removes)
            heapq.heappush(removes, enemy[i])
        else:
            # 현재 라운드가 무적권 대상보다 작음 → 그냥 싸움
            n -= enemy[i]

        if n < 0:
            # 이번 라운드(i)에서 전멸 → i-1까지가 최대
            return i  # i번째 라운드 실패 → i개 라운드 통과

    return len(enemy)  # 끝까지 성공하면 전체 라운드 길이
