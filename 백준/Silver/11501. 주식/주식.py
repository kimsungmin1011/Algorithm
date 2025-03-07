import sys

input = sys.stdin.readline

T = int(input().strip())  # 테스트 케이스 수
for _ in range(T):
    N = int(input().strip())  # 날짜 수
    prices = list(map(int, input().split()))

    max_price = 0
    total_profit = 0

    # 뒤에서부터 순회하면서 최대 이익 계산
    for i in range(N - 1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            total_profit += max_price - prices[i]

    print(total_profit)
