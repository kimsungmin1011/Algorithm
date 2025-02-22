n = int(input().strip())
stones = list(map(int, input().split()))
m = int(input().strip())
balls = list(map(int, input().split()))

dp = [False] * 40001
dp[0] = True  # 아무 추도 사용하지 않았을 때 무게 0은 True

for stone in stones:
    # 매 추를 추가할 때마다 새 상태를 복사해서 사용
    new_dp = dp[:]
    for w in range(40001):
        if dp[w]:
            # w 무게를 만들 수 있다면,
            # 1) w + stone
            if w + stone <= 40000:
                new_dp[w + stone] = True
            # 2) |w - stone|
            diff = abs(w - stone)
            new_dp[diff] = True
    dp = new_dp  # 이번 추를 반영한 상태로 업데이트

# m개의 구슬 무게를 확인하여 출력
for weight in balls:
    if weight <= 40000 and dp[weight]:
        print("Y", end=" ")
    else:
        print("N", end=" ")
