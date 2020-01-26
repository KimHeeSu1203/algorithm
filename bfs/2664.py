"""
참조 : https://dailyheumsi.tistory.com/48
"""
from collections import deque
from collections import defaultdict

n = int(input())
a,b = map(int,input().split())
t = int(input())

d = defaultdict(set)

for _ in range(t):
    x, y = map(int, input().split())
    d[x].add(y)
    d[y].add(x)

def bfs(a,b):
    q,visit = [a],{a}
    step = 0
    while q:
        size = len(q)

        for i in range(size):
            cur = q.pop(0)
            if cur == b:
                return step

            for j in d[cur]:
                if j not in visit:
                    visit.add(j)
                    q.append(j)
        step +=1
    return -1

print(bfs(a,b))





