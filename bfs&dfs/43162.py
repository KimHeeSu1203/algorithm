def solution(n, computers):
    answer = 0
    all = []
    for i in range(n):
        tmp = []
        for j in range(n):
            if computers[i][j] == 1:
                tmp.append(j)
        all.append(tmp)
    print(all)
    all = list(set(map(tuple,all)))
    return len(all)


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n,computers))