# 입력
N = list(input())
N = [int(i) for i in N]

# 내림차순으로 정렬
N.sort(reverse=True)

# 10의 배수 여부와 3의 배수 여부를 확인
if N[-1] == 0 and sum(N) % 3 == 0:
    for i in N:
        print(i, end='')
else:
    print(-1)
