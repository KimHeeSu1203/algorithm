"""
3 7
2 3 2 3 1 2 7
"""

N, K = map(int,input().split())

all_socket = list(map(int, input().split()))

now_socket = []
cnt = 0

for i in range(K):
    print("---------")
    print(now_socket)

    if all_socket[i] in now_socket:
        continue

    elif (all_socket[i] not in now_socket) & (len(now_socket)!=N) :
        now_socket.append(all_socket[i])

    else:
        cnt +=1
        for_count = [999 for _ in range(K)]
        for k in range(len(now_socket)):
            for_count[now_socket[k]-1] = all_socket[i+1:K].count(now_socket[k])

        change = now_socket.index(for_count.index(min(for_count))+1)
        now_socket[change] = all_socket[i]

print("---------")
print(now_socket)
print(cnt)


"""
Q.1700
여러 방법으로 풀어보다가 
고려 해야할 것이 지금 콘센트에 꽂혀있는지, 그리고 앞으로 꽂혀있을 것인지 라고 생각했음
그래서 만약에 뽑을 상황이 생기면 앞으로 꽂힐 애들은 제외하고 뽑는 방법(앞으로 나올 횟수가 많은 애)으로 했는데 틀렸음 왜인지 아직 모르겠음 
"""