Line = input()

stack = []
num = 0
for i in range(len(Line)):
    command = Line[i]

    if (i > 0):
        if (Line[i-1] == '(' and Line[i] == ')'):
            continue

    if (i < len(Line) - 1):
        #print("i, stack num",i,  stack, num)
        if (Line[i] == '(' and Line[i + 1] == ')'):
            num = num + len(stack)

        elif(Line[i] == '(' ) :# (인데 다음은 )가 아닌 경우
            stack.append(Line[i])

        elif(Line[i] == ')' ) :
            if(len(stack) > 0):
                num = num + 1
                stack.pop()
    else:
        num = num + len(stack)
print(num)





