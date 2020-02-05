from collections import defaultdict

def find(n, d):
    for i in range(n):
        for j in range(i+1, n):
            if len(d[i]) >= len(d[j]):
                width = len(d[j])
                if (d[j] == d[i][0:width]):
                    return -1
                    break

            elif len(d[i]) < len(d[j]):
                width = len(d[i])
                if (d[i] == d[j][0:width]):
                    return -1
                    break

    return 0

t = int(input())
for _ in range(t):
    n = int(input())
    d = defaultdict(str)
    for i in range(n):
        d[i] = input()

    result = find(n,d)

    if(result == 0):
        print("YES")

    else:
        print("NO")






