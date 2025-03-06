n, k = map(int, input().split())
coin = []  # 각 동전은 배수 관계

for i in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

count = 0
for i in coin:
    if k >= i:
        count += k // i
        k = k % (k // i * i)

print(count)
