from collections import defaultdict
import sys

def find(n, d):
    for i in range(n-1):
        width = len(d[i])
        if (d[i] in d[i+1][0:width]):
            return "NO"
            break
    return "YES"

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    d = []
    for i in range(n):
        d.extend(sys.stdin.readline().split())
    d.sort()
    #d.sort(key = lambda x : (len(x),x))
    print(find(n,d))







