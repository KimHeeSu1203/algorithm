from collections import defaultdict

def solution(genres, plays):
    all_song = []

    d = defaultdict(int)
    d_list = defaultdict(set)
    for i in range(len(genres)):
        song_count = plays[i]
        d_list[genres[i]].add(i)
        d[genres[i]] += song_count

    d = sorted(list(d.items()),key = lambda x : -x[1])
    d = list(map(lambda x : x[0],d))
    d_list = sorted(d_list.items(), key = lambda x: d.index(x[0]))

    print(d_list)
    print(d)

    all = []

    for i in d_list:
        num = list(i[1])
        tmp_list = []
        for j in num:
            tmp_list.append([j,plays[j]])
        all.append(tmp_list)

    print("all",all)

    tmp_answer = []
    for i in all:
        tmp_genre_sort = sorted(i,key = lambda x : (-x[1],x[0]))
        tmp_answer.append(tmp_genre_sort[0:2])

    answer = []
    for i in tmp_answer:
        tmp_answer = list(map(lambda x: x[0], i))
        answer.extend(tmp_answer)

    return answer


genres=["classic", "classic", "classic", "pop"]
plays =[500, 600, 150, 800, 2500]
# 장르 수 많은 순서, 재생 순서, 고유 순서 낮은 순
print(solution(genres, plays))