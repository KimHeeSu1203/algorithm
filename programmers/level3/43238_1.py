def solution(n, times):
    timeSum = times.copy()

    for i in range(n-1):
        minTime = timeSum.index(min(timeSum)) #제일 빨리 끝나는 곳 의미
        timeSum[minTime] += times[minTime]

    return min(timeSum)

n = 6
times = [7, 10]
print(solution(n,times))