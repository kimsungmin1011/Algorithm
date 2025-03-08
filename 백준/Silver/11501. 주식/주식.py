import sys

input = sys.stdin.readline

# 테스트 케이스 개수 입력
T = int(input())
for _ in range(T):
    N = int(input())  # 날짜 수 입력
    prices = list(map(int, input().split()))  # N일 동안의 주가 입력

    max_price = 0  # 현재까지 본 최고 주가 (뒤에서부터 순회)
    total_profit = 0  # 총 이익 저장 변수

    # 뒤에서부터 순회하면서 최대 이익 계산
    for i in range(N - 1, -1, -1):
        if prices[i] > max_price:
            # 현재 주가가 max_price보다 크다면 갱신
            max_price = prices[i]
        else:
            # 현재 주가가 max_price보다 작다면, 이익 계산
            total_profit += max_price - prices[i]

    # 최종 이익 출력
    print(total_profit)
