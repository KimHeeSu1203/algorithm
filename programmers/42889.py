# runtime error
def solution(N, stages):
    dict_stage = {}
    tmp_answer = [0 for _ in range(N+1)]
    answer = [0 for _ in range(N)]
    for stage in stages:
        for i in range(stage):
            tmp_answer[i] = tmp_answer[i] + 1

    for i in range(N):
        if tmp_answer[i] == 0:
            answer[i] = 0
        else:
            answer[i] = (tmp_answer[i]-tmp_answer[i+1]) / tmp_answer[i]

    answer = [i[0]+1 for i in sorted(enumerate(answer), key=lambda x: [-x[1],x[0]])]
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N,stages))