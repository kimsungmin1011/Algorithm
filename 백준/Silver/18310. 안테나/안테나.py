import sys

input = sys.stdin.readline

n = int(input())
house = list(map(int, input().split()))
house.sort()

if n % 2 != 0:
    print(house[n // 2])
else:
    first = house[n // 2 - 1]
    fd = 0
    for i in range(n):
        if i != n // 2 - 1:
            fd += abs(first - house[i])

    second = house[n // 2]
    sd = 0
    for i in range(n):
        if i != n // 2:
            sd += abs(second - house[i])

    if fd <= sd:
        print(first)
    else:
        print(second)
