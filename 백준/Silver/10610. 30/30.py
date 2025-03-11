# 입력
N = input()

# 자릿수를 리스트로 변환
numbers = [int(n) for n in N]

# 내림차순으로 정렬
numbers.sort(reverse=True)

# 10의 배수 여부와 3의 배수 여부를 확인
if 0 not in numbers or sum(numbers) % 3 != 0:
    print(-1)
else:
    print(''.join(map(str, numbers)))
