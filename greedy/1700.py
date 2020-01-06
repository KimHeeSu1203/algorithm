"""
3 7
2 3 2 3 1 2 7
"""

N, K = map(int,input().split())

all_socket = list(map(int, input().split()))

now_socket = [] # 길이 3 아닌것도 고려 해야

cnt = 0

for i in range(K):
    if all_socket[i] in now_socket:
        continue

    elif (all_socket[i] not in now_socket) & (len(now_socket)!=N) :
        now_socket.append(all_socket[i])
        #print("111111")

    else:
        cnt +=1
        for_count = [999 for _ in range(K)]
        for k in range(len(now_socket)):
            #print(all_socket[i+1:K])
            #print(all_socket[i+1:K].count(now_socket[k]))
            #print(now_socket[k])
            for_count[now_socket[k]-1] = all_socket[i+1:K].count(now_socket[k])
        #print("xxxxxx")
        #print("forcount",for_count)
        #print(for_count.index(min(for_count)))

        change = now_socket.index(for_count.index(min(for_count))+1)
        now_socket[change] = all_socket[i]
        #now_socket[)] = all_socket[i]
    #print(now_socket)

print(cnt)
"""
tmp_socket = []
socket = []
for i in range(len(all_socket)):
    if i in tmp_socket
    tmp_socket.append(i)
    
"""
"""
using_group = []

for i in range(N-1,K):
    tmp_group = socket[i-(N-1):(i+1)]
    tmp_group = list(set(tmp_group))
    using_group.append(tmp_group)

print(using_group)
inter = []
for i in range(0,len(using_group)-1):
    print(list(set(using_group[i]).intersection(using_group[i+1])))
    temp_inter = len(list(set(using_group[i]).intersection(using_group[i+1])))
    temp_inter =len(using_group[i+1]) - temp_inter
    print(temp_inter)
    inter.append(temp_inter)

print(inter)
print(sum(inter))

## 문제가 겹치는 것들을 뺴버리니까
"""