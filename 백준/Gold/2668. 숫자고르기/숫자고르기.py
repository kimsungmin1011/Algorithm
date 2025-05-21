import sys

input = sys.stdin.readline


# DFS 함수: 현재 노드 v에서 시작하여 자기 자신(i)으로 돌아오는 사이클 여부 확인
def dfs(v, i):
    # 현재 노드 방문 처리
    visited[v] = True
    # 현재 노드가 가리키는 다음 노드 w
    w = data[v]
    # 다음 노드를 아직 방문하지 않았다면 DFS 계속 진행
    if not visited[w]:
        dfs(w, i)
    # 다음 노드가 이미 방문한 노드이고, 시작 노드 i와 같다면 사이클 발생 → 결과에 추가
    elif visited[w] and w == i:
        result.append(w)


n = int(input())
data = [0] + [int(input()) for _ in range(n)]
result = []

# 모든 노드에 대해 DFS 수행하여 사이클 여부 탐색
for i in range(1, n + 1):
    # DFS 마다 방문 배열 초기화 (각 노드 기준으로 탐색)
    visited = [False] * (n + 1)
    dfs(i, i)

# 오름차순 정렬
result.sort()

# 결과에 포함된 숫자 개수 출력
print(len(result))

# 결과 숫자들 오름차순 출력
for i in result:
    print(i)
