import heapq
import sys


n = sys.stdin.readline().strip()
heap = []

for _ in range(int(n)):
    x = sys.stdin.readline().strip()
    x = int(x)
    if x == 0 :
        if len(heap) == 0:
            print("0")
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,x)