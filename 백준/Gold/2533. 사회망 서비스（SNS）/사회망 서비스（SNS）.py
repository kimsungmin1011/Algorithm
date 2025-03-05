import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력 받기
n = int(input().strip())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# DP 배열 초기화
# dp[u][0] → u가 얼리 어답터가 아닐 때, u의 서브트리에서 필요한 최소 얼리 어답터 수
# dp[u][1] → u가 얼리 어답터일 때, u의 서브트리에서 필요한 최소 얼리 어답터 수
dp = [[-1, -1] for _ in range(n + 1)]


# 트리 DP (DFS 활용)
def dfs(node):
    dp[node][0] = 0  # node가 얼리 어답터가 아닐 때
    dp[node][1] = 1  # node가 얼리 어답터일 때

    for child in tree[node]:
        if dp[child][0] == -1 and dp[child][1] == -1:  # 방문하지 않은 자식 노드 탐색
            dfs(child)
            # 내가 얼리 어답터가 아니면, 자식은 반드시 얼리 어답터
            dp[node][0] += dp[child][1]
            # 내가 얼리 어답터면, 자식은 얼리 어답터일 수도 있고 아닐 수도 있음
            dp[node][1] += min(dp[child])


# 루트는 1번 노드라고 가정
dfs(1)

# 최소 얼리 어답터 수 출력
print(min(dp[1]))
