from collections import defaultdict
t = int(input())

for _ in range(t):
    N, M = map(int,input().split())
    tmp_imp = input().split()
    imp = []
    for k in range(N):
        numbering = [k,int(tmp_imp[k])]
        imp.append(numbering)
    for i in range(len(imp)):
        sort_imp = sorted(imp[i:],key = lambda x : [x[1]], reverse=True)
        while(imp[i] != sort_imp[0]):
            imp.append(imp.pop(i))

    for i in range(N):
        a,b = imp[i]
        if a == M:
            print(i+1)