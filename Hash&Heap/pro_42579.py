
def solution(genres, plays):
    answer_dict = {}
    sum_dict = {}
    answer_list = []

    for i in range(len(genres)):
        if genres[i] not in sum_dict:
            sum_dict[genres[i]] = 0
        sum_dict[genres[i]] = plays[i] + sum_dict[genres[i]]


    for i in range(len(genres)):
        if genres[i] not in answer_dict:
            answer_dict[genres[i]] = []
        answer_dict[genres[i]].append([i,plays[i],sum_dict[genres[i]]])

    for i in answer_dict:
        answer_dict[i].sort(key= lambda x:[-x[1],x[0]])
        answer_list.extend(x for x in answer_dict[i][:2])
    answer_list.sort(key=lambda x : [-x[2],-x[1],x[0]])
    answer = []
    for i in range(len(answer_list)):
        answer.append(answer_list[i][0])

    return answer



genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres,plays))

"""
answer_dict[i].sort(key=lambda x: [-x[2],-x[1],x[0]])
print("22222", answer_dict)
answer_list.extend(x[0] for x in answer_dict[i][:2])
"""