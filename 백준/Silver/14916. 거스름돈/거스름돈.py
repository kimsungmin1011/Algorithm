n = int(input())

# n을 5로 나누어 최대한의 5원짜리 동전의 개수를 구한다.
max_five = n // 5
remainder = n % 5

while max_five >= 0:
    # 2원짜리 동전으로 나머지 금액을 거슬러 줄 수 있는 경우
    if remainder % 2 == 0:
        print(max_five + remainder // 2)
        break
    # 2원짜리 동전으로 나머지 금액을 거슬러 줄 수 없는 경우 5원짜리 동전의 개수를 줄인다.
    max_five -= 1
    remainder += 5
else:
    print(-1)
