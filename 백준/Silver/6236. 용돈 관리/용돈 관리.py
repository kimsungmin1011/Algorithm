n, m = map(int, input().split())
daily = []

for i in range(n):
    daily.append(int(input()))

start = max(daily)
end = sum(daily)
answer = 0

while start <= end:
    mid = (start + end) // 2  # 1회 인출 금액
    wallet = 0  # 현재 남아있는 돈
    count = 0  # 인출 횟수

    for day in daily:
        if wallet >= day:
            # 남은 돈만으로 day날 생활 가능하다면
            wallet -= day
        else:
            # 남은 돈 부족하면 mid원만큼 새로 인출하고 day날 이용 금액 빼줌
            wallet = mid - day
            count += 1  # 인출 횟수 +1

    # 인출 횟수가 m번 이하면 가능, 금액 줄여서 다시 탐색
    if count <= m:
        answer = mid
        end = mid - 1
    else:
        # 인출 횟수가 m번보다 많다면 금액 늘려서 다시 탐색
        start = mid + 1

print(answer)
