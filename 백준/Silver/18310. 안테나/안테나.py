import sys

input = sys.stdin.readline

n = int(input())  # 집의 개수 입력
house = list(map(int, input().split()))  # 집들의 위치 입력
house.sort()  # 집의 위치를 오름차순 정렬

if n % 2 != 0:  # 집의 개수가 홀수일 경우
    print(house[n // 2])  # 중앙값 출력
else:  # 집의 개수가 짝수일 경우
    print(house[n // 2 - 1])  # 중앙값 출력
