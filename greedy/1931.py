"""
틀린 이유, 소팅 시에 x[1], x[0]순으로 소팅이 두번 되었어야 했는데, 소팅을 한번만 해놨기 때문에 답이 잘 안나왔음
"""
N = int(input())
all=[]

for _ in range(N):
    start,end = map(int,input().split())
    all.append([start,end])

batch=[]
batch.append([0,0])

all.sort(key=lambda x : [x[1], x[0]])
for i in range(len(all)):
    if all[i][0] >= batch[-1][1]:
        batch.append(all[i])

print(len(batch)-1)
