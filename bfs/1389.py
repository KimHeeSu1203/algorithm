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

n,m = map(int,input().split())
relationship=list()
relationship_matrix = [[0 for col in range(n)] for row in range(n)]
visit_matrix = [[0 for col in range(n)] for row in range(n)]

for i in range(m):
    k = input().split()
    relationship.append(k)

#print(relationship)
for i in range(n):
    visit_matrix[i][i] = 1

for i in range(m):
    ab = int(relationship[i][0])-1
    ba = int(relationship[i][1])-1
    relationship_matrix[ab][ba] = 1
    relationship_matrix[ba][ab] = 1

sum = 0
queue = list()
for i in range(n): #1번째 사람부터 해
    for j in range(n): # 첫번째 사람 순서대
        while visit_matrix[i] != [1,1,1,1,1]: #전부 다 방문할 때까
            if i!=j & relationship_matrix[i][j] == 1: #친구인 사이이면
                visit_matrix[i][j] = 1
                queue.append(j)
                sum +=1

                for k in


