answer = 0

n = int(input())
ask = []  # 민혁이의 질문 리스트

for _ in range(n):
    ask.append(list(map(int, input().split())))

ball_list = []
current = []
visited = [False for _ in range(10)]


# 1부터 9까지 서로 다른 숫자 세 개로 구성된 세 자리 수를 모두 구하는 백트래킹 함수
def dfs():
    if len(current) == 3:
        ball_list.append("".join(current))
        return

    for i in range(1, 10):
        if visited[i] == False:
            visited[i] = True
            current.append(str(i))
            dfs()
            current.pop()
            visited[i] = False


dfs()

# 모든 숫자 완전 탐색
for i in range(len(ball_list)):
    candidate_ball = ball_list[i]  # 현재 숫자
    flag = True
    # 민혁이의 n개 질문 모두 검사
    for j in range(n):
        # 현재 민혁이가 얘기한 숫자, 스트라이크 개수, 볼 개수
        minhyuk_ask, minhyuk_strike, minhyuk_ball = (
            str(ask[j][0]),
            ask[j][1],
            ask[j][2],
        )
        strike, ball = 0, 0  # 스트라이크, 볼 개수 카운트
        for k in range(3):
            # 현재 숫자와 민혁이가 얘기한 숫자의 k번째 수가 같다면
            if minhyuk_ask[k] == candidate_ball[k]:
                strike += 1
            # 민혁이가 얘기한 숫자의 k번째 수가 현재 숫자의 다른 위치에 있다면
            elif minhyuk_ask[k] in candidate_ball:
                ball += 1
        # 만약 현재 숫자의 SB값이 영수가 답한 SB값과 다르다면 다음 숫자로
        if strike != minhyuk_strike or ball != minhyuk_ball:
            flag = False
            break
    # 민혁이의 모든 질문에 똑같이 답했다면 가능성 있는 답
    if flag == True:
        answer += 1


print(answer)
