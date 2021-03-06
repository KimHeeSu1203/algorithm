"""
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
import sys

t = int(input())
q = []

for _ in range(t):
    command = sys.stdin.readline().split()
    size = len(q)
    if "push" in command[0]:
        q.append(command[1])

    if command[0] == "pop":
        if size > 0:
            print(q[size-1])
            q.pop()
        else:
            print("-1")

    if command[0] == "top":
        if q:
            print(q[size-1])
        else:
            print("-1")

    if command[0] == "size":
        print(size)

    if command[0] == "empty":
        if size == 0 :
            print("1")
        else :
            print("0")
