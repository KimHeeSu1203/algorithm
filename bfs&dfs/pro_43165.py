answer = 0
def DFS(numbers,i,s,t):
    global answer
    if i == len(numbers): #끝까지 도달하면
        if s == t: # 같음
            answer = answer + 1
            return
        else: #다름
            return
    else: #끝까지 도달못하면
        DFS(numbers,i+1,s+numbers[i],t)
        DFS(numbers,i+1,s-numbers[i],t)


def solution(numbers,target):
    global answer
    DFS(numbers, 0, 0, target)
    return answer


numbers = [1,1,1,1,1]
target = 3
answer = solution(numbers,target)