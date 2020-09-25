def solution(n, times):
    answer = []
    for i in range(1,n+1):
        for j in range(len(times)):
            answer.append(i*times[j])

    answer = sorted(answer)
    return answer[n-1]


n = 6
times = [7, 10]
print(solution(n,times))