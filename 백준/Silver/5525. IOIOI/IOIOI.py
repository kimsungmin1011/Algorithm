n = int(input())
m = int(input())

s = list(input())

current = "I"
current += "OI" * n
c_len = len(current)

answer = 0

for i in range(m - c_len + 1):
    if "".join(s[i : i + c_len]) == current:
        answer += 1

print(answer)
