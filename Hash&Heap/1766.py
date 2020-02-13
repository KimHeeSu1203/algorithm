from collections import defaultdict
import sys

n,m = map(int, sys.stdin.readline().split())

list = [[] for _ in range(n+1)]
count = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    list[a].append(b)
    list[a].sort()
    count[b] += 1

final_list = []
real_final_list = []
for i in range(1,n+1):
    if (count[i] == 0): # 우선순위 문제 없으면
        final_list.append(i)
        while (final_list):
            num = final_list.pop(0)
            real_final_list.append(num)
            for j in range(len(list[num])):
                count[list[num][j]] -= 1  # 1씩 깎아줌
                if count[list[num][j]] == 0:
                    final_list.append(list[num][j])


for elem in real_final_list:
    print(elem, end = " ")