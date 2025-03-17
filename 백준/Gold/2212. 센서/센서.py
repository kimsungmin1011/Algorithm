n = int(input())
k = int(input())

sensor = list(map(int, input().split()))
sensor.sort()

distance = []

for i in range(n - 1):
    distance.append(abs(sensor[i] - sensor[i + 1]))

distance.sort()

for _ in range(k - 1):
    if len(distance) >= 1:
        distance.pop()

print(sum(distance))
