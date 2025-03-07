import sys

input = sys.stdin.readline

T = int(input().strip())  # 테스트 케이스 수

for _ in range(T):
    N = int(input().strip())  # 지원자 수
    candidates = [tuple(map(int, input().split())) for _ in range(N)]

    # 1. 서류 등수를 기준으로 오름차순 정렬
    #    (기본 정렬 기준이 튜플의 첫 요소 → 서류 등수)
    candidates.sort()

    # 2. 첫 번째 사람은 서류 등수가 가장 좋으므로 무조건 선발
    count_selected = 1
    # 첫 번째 사람의 면접 등수를 "최소값"으로 설정
    min_interview_rank = candidates[0][1]

    # 3. 두 번째 사람부터 면접 등수 확인
    for i in range(1, N):
        # 새 지원자의 면접 등수가 지금까지의 최소 면접 등수보다 더 좋다면(더 작은 수라면)
        if candidates[i][1] < min_interview_rank:
            count_selected += 1  # 선발
            min_interview_rank = candidates[i][1]  # 최소 면접 등수 갱신

    print(count_selected)
