def solution(s):
    s = [int(i) for i in s]
    new_s = []
    count = 0
    kill_zero = 0

    while True:
        if len(s) == 1:
            return [count, kill_zero]

        len_s = 0
        for i in s:
            if i == 1:
                len_s += 1
            else:
                kill_zero += 1

        new_s = []
        while len_s > 0:
            mok = len_s // 2
            namuji = len_s % 2
            new_s.append(namuji)
            len_s = mok

        new_s.reverse()
        s = new_s
        count += 1
