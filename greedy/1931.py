"""
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.
"""

def sortrule_selection(item):
    return item[1]

N = int(input())
all=[]

for _ in range(N):
    start,end = map(int,input().split())
    all.append([start,end])

batch=[]
batch.append([0,0])

all.sort(key=sortrule_selection)

for i in range(len(all)):
    if all[i][0] < batch[-1][1]:
        continue
    batch.append(all[i])

print(len(batch)-1)
