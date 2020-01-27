
from collections import deque
import sys

t = int(input())
q = deque()
for k in range(t):
    command = sys.stdin.readline().split()
    size = len(q)
    if "push" in command[0]:
        q.append(command[1])

    if command[0] == "pop":
        if size > 0:
            print(q[0])
            q.popleft()
        else:
            print("-1")

    if command[0] =="size":
        print(size)

    if command[0] == "empty":
        if size > 0:
            print("0")
        else:
            print("1")

    if command[0] == "front":
        if size > 0:
            print(q[0])
        else:
            print("-1")

    if command[0] == "back":
        if size > 0:
            print(q[size-1])
        else:
            print("-1")

