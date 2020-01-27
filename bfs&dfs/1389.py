"""
첫째 줄에 유저의 수 N (2 ≤ N ≤ 100)과 친구 관계의 수 M (1 ≤ M ≤ 5,000)이 주어진다.
둘째 줄부터 M개의 줄에는 친구 관계가 주어진다. 친구 관계는 A와 B로 이루어져 있으며, A와 B가 친구라는 뜻이다.
A와 B가 친구이면, B와 A도 친구이며, A와 B가 같은 경우는 없다.
친구 관계는 중복되어 들어올 수도 있으며, 친구가 한 명도 없는 사람은 없다. 또, 모든 사람은 친구 관계로 연결되어져 있다.
5 5
1 3
1 4
4 5
4 3
3 2
"""
import queue
import operator

n,m = map(int,input().split())
relationship=list()
queue = [[] for i in range(n)]
relationship_matrix = [[0 for col in range(n)] for row in range(n)]

for i in range(m): # 관계 정보 받아온
    k = input().split()
    relationship.append(k)

for i in range(m):
    ab = int(relationship[i][0])-1
    ba = int(relationship[i][1])-1
    relationship_matrix[ab][ba] = 1
    relationship_matrix[ba][ab] = 1

sum = [[0 for col in range(n)] for row in range(n)]
sum_sum = [0 for col in range(n)]
all_friends = [i for i in range(n)]

for i in range(n):
    flag1 = len(queue[i])
    queue[i].append(i)
    flag2 = len(queue[i])
    tmp_sum = 0
    while sorted(queue[i]) != all_friends:

        tmp_sum +=1
        for j in range(flag1,flag2):
            #queue에 각자의 친구를 더하는 것
            friend = queue[i][j]
            #friend_friend = list()
            for p in range(n):
                if (relationship_matrix[friend][p] == 1) & (p not in queue[i]): #이 사람의 친구 정보를 담는데 나한테 아직 없으면
                    queue[i].append(p)
                    sum[i][p] = tmp_sum
        flag1 = flag2
        flag2 = len(queue[i])


for i in range(n):
    for j in range(n):
        sum_sum[i] += sum[i][j]

index = sum_sum.index(min(sum_sum))
index +=1

print(index)




