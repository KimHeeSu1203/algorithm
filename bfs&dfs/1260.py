"""
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
"""
from collections import defaultdict
def dfs(d,V):

    stack = list()
    d_visit = list()

    stack.append(V)

    while stack:
        cur = stack.pop()
        if cur not in d_visit:
            d_visit.append(cur)
            connect = sorted(list(d[cur]))
            connect.reverse()
            stack.extend(connect)

    print(" ".join(map(str, d_visit)))



def bfs(d,V):

    queue = [V]

    d_visit = list()
    d_visit.append(V)

    while queue:
        cur = queue.pop(0)
        connect = sorted(list(d[cur]))
        for i in connect:
            if i not in d_visit:
                queue.append(i)
                d_visit.append(i)

    print(" ".join(map(str, d_visit)))

N, M, V = map(int, input().split()) # V는 시작
d = defaultdict(set)

for _ in range(M):
    a,b = map(int,input().split())
    d[a].add(b)
    d[b].add(a)

dfs(d,V)
bfs(d,V)

