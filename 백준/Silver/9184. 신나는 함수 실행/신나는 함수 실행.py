import sys

sys.setrecursionlimit(10**5)

graph = dict()


def w(x, y, z):
    word = "f" + str(x) + "s" + str(y) + "t" + str(z)
    if word in graph:
        return graph[word]
    else:
        if x <= 0 or y <= 0 or z <= 0:
            graph[word] = 1
        elif x > 20 or y > 20 or z > 20:
            graph[word] = w(20, 20, 20)
        elif x < y < z:
            graph[word] = w(x, y, z - 1) + w(x, y - 1, z - 1) - w(x, y - 1, z)
        else:
            graph[word] = (
                w(x - 1, y, z)
                + w(x - 1, y - 1, z)
                + w(x - 1, y, z - 1)
                - w(x - 1, y - 1, z - 1)
            )

        return graph[word]


while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    print(f"w({a}, {b}, {c}) =", w(a, b, c))
