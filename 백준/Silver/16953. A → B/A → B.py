A, B = map(int, input().split())

count = 0

while B > A:
    # 짝수인 경우
    if B % 2 == 0:
        B //= 2
        count += 1
        
    # 마지막 숫자가 1인 경우
    elif B % 10 == 1:
        B //= 10
        count += 1
        
    # 그 외의 경우
    else:
        break

if A == B:
    print(count + 1)
else:
    print(-1)
