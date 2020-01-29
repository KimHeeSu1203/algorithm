"""
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
"""
from collections import defaultdict
from collections import deque

def dfs(d,d_visit,V):
    for i in range(1,N+1):
        d_visit[i] = 0
    stack = [V]
    temp_stack = [V]
    d_visit[V] = 1

    while stack:
        cur = stack.pop()
        connect = sorted(list(d[cur]))
        for i in connect:
            if(d_visit[i] == 0):
                stack.append(i)
                temp_stack.append(i)
                d_visit[i] = 1

    print(temp_stack)


def bfs(d,d_visit, V):
    for i in range(1,N+1):
        d_visit[i] = 0

    queue = deque()
    temp_queue = []

    queue.append(V)
    temp_queue.append(V)

    d_visit[V] = 1

    while queue:
        cur = queue.popleft()
        connect = sorted(list(d[cur]))
        for i in connect:
            if (d_visit[i] == 0):
                queue.append(i)
                temp_queue.append(i)
                d_visit[i] = 1

    print(temp_queue)




N, M, V = map(int, input().split()) # V는 시작
d = defaultdict(set)
d_visit = defaultdict(set)
for _ in range(M):
    a,b = map(int,input().split())
    d[a].add(b)
    d[b].add(a)

dfs(d,d_visit,V)
bfs(d,d_visit,V)

