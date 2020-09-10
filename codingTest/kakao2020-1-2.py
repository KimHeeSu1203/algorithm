def testRight(p):
    flag = True
    stack = []
    for i in range(len(p)):
        if p[i] == '(':
            stack.append('(')
        elif p[i] == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                flag = False
                return flag
    return flag

def makeRight(p):
    if len(p) == 0:
        return p

    count_L=0
    count_R=0
    for i in range(len(p)):
        if p[i] == '(':
            count_L +=1
        elif p[i] == ')':
            count_R +=1

        if (count_L > 0) & (count_R > 0) & (count_L == count_R):
            breakNum = i
            break

    u = p[:breakNum+1]
    v = p[breakNum+1:]

    testArr = []

    if testRight(u) == True:
        testArr.append(u)
        testArr.append(makeRight(v))

    else:

        testArr.append('(')
        testArr.append(v)
        testArr.append(')')
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == '(':
                u = u[:i] + ')' + u[i+1:]
            else:
                u = u[:i] + '(' + u[i+1:]
        testArr.append(u)

    return "".join(testArr)

def solution(p):
    if testRight(p) == True:
        return p
    else:
        return makeRight(p)


s = "(()))()(()"
print(solution(s))