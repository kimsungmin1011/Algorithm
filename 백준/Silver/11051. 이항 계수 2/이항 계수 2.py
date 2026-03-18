n, k = map(int, input().split())

first = 1
secound = 1
third = 1

for i in range(1, n + 1):
    first *= i

for i in range(1, n - k + 1):
    secound *= i

for i in range(1, k + 1):
    third *= i

print(int(first // (secound * third) % 10007))
