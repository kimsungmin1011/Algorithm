def solution(genres, plays):
    answer = []

    song = {}
    song_total = {}
    for i in range(len(genres)):
        if genres[i] not in song:
            song[genres[i]] = [(plays[i], i)]
            song_total[genres[i]] = plays[i]
        else:
            song[genres[i]].append((plays[i], i))
            song_total[genres[i]] += plays[i]

    key_list = [i for i in song]
    key_list.sort(key=lambda x: song_total[x], reverse=True)

    for i in key_list:
        count = 0
        song[i].sort(key=lambda x: (-x[0], x[1]))

        for j in song[i]:
            if count == 2:
                break
            answer.append(j[1])
            count += 1

    return answer
