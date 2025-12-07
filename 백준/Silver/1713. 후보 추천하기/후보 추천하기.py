import sys

input = sys.stdin.readline

N = int(input())  # 사진틀 개수
M = int(input())  # 전체 추천 횟수
recs = list(map(int, input().split()))  # 추천받은 학생 번호들

# frame[student] = [recommend_count, posted_time]
frame = {}

time = 0  # 들어온 순서를 기록하기 위한 시간(카운터)

for student in recs:
    time += 1  # 새로운 추천이 들어올 때마다 시간 증가

    # 1. 이미 사진틀에 있는 학생이라면 추천 수만 증가
    if student in frame:
        frame[student][0] += 1
        continue

    # 2. 사진틀에 없고, 아직 자리가 남았다면 그냥 추가
    if len(frame) < N:
        frame[student] = [1, time]
        continue

    # 3. 사진틀에 없고, 자리가 없다면 한 명을 내림
    #    기준: (추천수 오름차순, 게시된 시간 오름차순)
    #    min으로 하나 선택
    remove_student = min(
        frame.items(), key=lambda item: (item[1][0], item[1][1])  # (추천수, 시간)
    )[0]

    # 선택된 학생 제거
    frame.pop(remove_student)

    # 새 학생 추가
    frame[student] = [1, time]

# 마지막에 사진틀에 남아 있는 학생 번호를 오름차순으로 출력
result = sorted(frame.keys())
print(*result)
