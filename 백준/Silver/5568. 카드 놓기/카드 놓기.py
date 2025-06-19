from itertools import permutations

n = int(input())
k = int(input())

cards = []

for i in range(n):
    cards.append(input())

total_save = set()

for array in permutations(cards, k):
    word = "".join(array)
    total_save.add(word)

print(len(total_save))
