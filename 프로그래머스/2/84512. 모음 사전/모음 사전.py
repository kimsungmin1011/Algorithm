moum = ["A", "E", "I", "O", "U"]

array_list = []
array=[]

def dfs(idx):
    if idx!=0:
        array_list.append("".join(array[:]))
    
    if idx == 5:
        return

    for i in range(5):
        array.append(moum[i])
        dfs(idx + 1)
        array.pop()


def solution(word):
    dfs(0)
    return array_list.index(word) + 1

print(solution("AAAE"))