list = input()

stack = []

num = 0
for i in range(len(list)):
    if num == 0 and list[i] == '(':
        num += 1
        temp_line = []

    elif num == 1 and list[i] == ')':
        num -= 1

    elif num == 0 and list[i] != '(' and list[i] != ')':
        stack.append(temp_line)

    else: # 다른 애들 나오면
        temp_line.extend(list[i])

    if i != 0 and num == 0:
        stack.append(temp_line)

print("stack : ", stack)
"""
for i in range(len(list)):
    if  list[i] != '(' and list[i] != ')': ## i = 1인 경우 감안하기!!
        temp_line.extend(list[i])

    elif len(temp_line) == 0 and list[i] == '(':
        continue

    elif len(temp_line) != 0 and list[i] == '(':
        stack.append(temp_line)
        temp_line = []

    elif len(temp_line) == 0 and list[i] == ')':
        continue

    elif len(temp_line) != 0 and list[i] == ')':
        stack.append(temp_line)
        temp_line = []


print("stack : ", stack)

all = []
temp_all = []
for i in range(len(stack)):
    if len(stack[::-1][i]) == 1:
        print("stack[::-1][i]",i, stack[::-1][i])
        notation = stack[::-1][i].pop(0)


    else:
        print("stack[::-1][i]",i, stack[::-1][i])
        notation = stack[::-1][i].pop(1)
        temp_all.extend(stack[::-1][i])

print("all : ")
for k in range(len(all)):
    print(all[k])


"""