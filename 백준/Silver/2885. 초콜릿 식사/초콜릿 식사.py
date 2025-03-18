import sys

input = sys.stdin.readline

K = int(input())  # 먹어야 하는 초콜릿 조각 개수
x = [2**i for i in range(21)]  # 초콜릿 선택용

# K개 조각보다 큰 초콜릿의 최소 크기 구하기
for i in x:
    if K <= i:
        choco = i
        break

cnt = 0  # 초콜릿 쪼갠 횟수
temp = choco  # 쪼개줄 임시 초콜릿

if K != choco:  # 통초콜릿의 조각 개수가 다르면
    while K:  # 0이 될 때까지 쪼개보자
        temp //= 2  # 반으로 쪼갬
        if K >= temp:  # 쪼갠 조각 개수가 원하는 개수보다 작으면
            K = K - temp  # 우선 쪼갠 조각 개수만큼 먹고
            cnt += 1  # 쪼갠 수 증가
        else:  # 아니면
            cnt += 1  # 쪼개기만하기

# (가장 작은 통초콜릿 크기, 쪼갠 횟수)
print(choco, cnt)
