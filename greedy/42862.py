def solution(n, lost, reserve):
    all_user = [0 for _ in range(n)]
    for i in range(len(lost)):
        all_user[lost[i]-1] += -1

    #print(all_user)
    for i in range(len(reserve)):
        all_user[reserve[i]-1] += 1
    #print(all_user)
    for i in range(n-1):
        if (all_user[i] + all_user[i+1]) == 0 :
            all_user[i] = 0
            all_user[i+1] = 0



    answer = 0

    for i in range(n):
        if (all_user[i] >= 0):
            answer += 1

    #print(all_user,"all")
    return answer

print(solution(3,[3],[1]))