
def VPS(PS):
    stack = list()
    for _ in range(len(PS)):
        cur = PS.pop()
        #print("stack", stack)
        if (cur == ')') :
            stack.append(cur)

        else:
            if len(stack) == 0:
                return "NO"
            else:
                stack.pop()

    if len(stack) == 0:
        return "YES"

    else:
        return "NO"


N = int(input())
for _ in range(N):
    PS = list(input())
    print(VPS(PS))


