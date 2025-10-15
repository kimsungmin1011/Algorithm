def solution(h1, m1, s1, h2, m2, s2):
    def to_seconds(h, m, s):
        return h * 3600 + m * 60 + s

    def F(t):
        # (0, t] 동안의 겹침 횟수 (초-분 + 초-시 - 삼중)
        return (59 * t) // 3600 + (719 * t) // 43200 - (t // 43200)

    t1 = to_seconds(h1, m1, s1)
    t2 = to_seconds(h2, m2, s2)

    # 날짜 넘어감 보정
    if t2 < t1:
        t2 += 86400

    ans = F(t2) - F(t1)

    # 시작점이 삼중겹침(정각 12시)일 경우 +1
    if t1 % 43200 == 0:
        ans += 1

    return ans