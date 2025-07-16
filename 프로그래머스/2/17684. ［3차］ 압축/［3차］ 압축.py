def solution(msg):
    answer = []
    word_list = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    final_i = -100
    for i in range(len(msg)):
        if i <= final_i:
            continue
        current = []
        for j in range(i, len(msg)):
            current.append(msg[j])
            c_word = "".join(current)
            if c_word not in word_list:
                word_list.append(c_word)
                current.pop()
                c_word = "".join(current)
                answer.append(word_list.index(c_word) + 1)
                final_i = j - 1
                break
            elif j == len(msg) - 1 and c_word in word_list:
                answer.append(word_list.index(c_word) + 1)
                final_i = j

    return answer
