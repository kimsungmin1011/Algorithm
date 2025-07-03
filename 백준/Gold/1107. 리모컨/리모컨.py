import sys

sys.setrecursionlimit(100000)

n = int(input())  # 이동하려는 채널
m = int(input())  # 고장난 버튼 수
broken = set()
if m > 0:
    line = set(map(int, input().split()))
    broken = line  # 고장난 버튼을 집합으로 저장


# 현재 채널에서 +, - 버튼으로만 이동하는 경우
min_time = abs(n - 100)


# 숫자 버튼을 눌러 채널로 이동하는 경우를 확인
def is_possible(channel):
    for digit in str(channel):
        if int(digit) in broken:
            return False
    return True


# 0부터 1,000,000까지 가능한 모든 채널을 탐색
for channel in range(1000000):
    if is_possible(channel):  # 채널을 누를 수 있는 경우
        # 버튼을 누른 횟수 + 이동 버튼 횟수
        min_time = min(min_time, len(str(channel)) + abs(channel - n))

print(min_time)
