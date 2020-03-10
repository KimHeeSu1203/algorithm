def solution(progresses, speeds):
    answer = []

    while(progresses):
        flag = False
        now = len(progresses)
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while(progresses and progresses[0]>=100):
            flag = True
            progresses.pop(0)
            speeds.pop(0)

        next = len(progresses)
        if flag == True:
            answer.append(now-next)
    return answer


progresses = [93,30,55]
speeds = [1,30,5]
print(solution(progresses, speeds))