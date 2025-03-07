# 1080번 행렬

n, m = map(int, input().split())
count = 0
non_answer = 0

# 변환할 행렬과 정답 행렬 입력받기
change_matrix = [list(map(int, input())) for _ in range(n)]
answer_matrix = [list(map(int, input())) for _ in range(n)]


# 3x3 행렬 변환 함수 생성
def convert_matrix(i, j, arr):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            arr[x][y] = 1 - arr[x][y]


# 차례대로 원소를 받아
for i in range(n - 2):
    for j in range(m - 2):
        # 변환할 행렬의 원소가 정답 행렬과 불일치시 3x3 행렬 값변환
        if change_matrix[i][j] != answer_matrix[i][j]:
            convert_matrix(i, j, change_matrix)
            count += 1

# 변환할 행렬과 정답 행렬 비교 검증
for i in range(n):
    for j in range(m):
        # 불일치시 -1을 출력
        if change_matrix[i][j] != answer_matrix[i][j]:
            non_answer = -1

# 정답 출력
if non_answer == -1:
    print(-1)
else:
    print(count)
