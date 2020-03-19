def dfs(n,computers,visit,start):
    tmp = [start] # 친구인 애들 담는
    while(tmp):
        x = tmp.pop(0)
        if visit[x]==0:
            visit[x]=1
        for i in range(n):
            if(computers[x][i]==1) and (visit[i]==0):
                tmp.append(i)


def solution(n, computers):
    answer = 0
    visit = [0]*n
    start = 0
    while 0 in visit:
        if visit[start] == 0:
            dfs(n,computers,visit,start)
            answer +=1
        start+=1
    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 0, 1]]
print(solution(n,computers))