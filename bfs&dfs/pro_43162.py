def solution(n, computers):
    answer = 0
    visited = []


    def dfs(start):
        stack = [start]
        while stack:
            num = stack.pop()
            if num not in visited:
                visited.append(num)
                for i in range(len(computers[start])):
                    if (computers[num][i] == 1) and (i not in visited):
                        stack.append(i)

    for i in range(len(computers)):
        if i not in visited:
            dfs(i)
            answer = answer + 1

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,computers))




"""
def bfs(n,computers,i,tmp_answer):
    global answer
    for k in range(len(computers[i])): # i번째랑 친구라하면
        if (computers[i][k] == 1) & (i != k):
            if(computers[i][k] not in tmp_answer):
                tmp_answer.add(computers[i][k])
                bfs(n,computers,k,tmp_answer)
            else:
                return
            answer.append(tmp_answer)
        else: #친구 아니라 하면
            tmp_answer = set()
            bfs(n, computers, k, tmp_answer)


def solution(n,computers):
    global answer
    tmp_answer = set()
    bfs(n,computers,0,tmp_answer)
    return answer
"""