def solution(arrangement):
    answer = 0
    stack = []

    for i, x in enumerate(arrangement):
        if x == '(':
            stack.append(x)
        elif x == ')'and arrangement[i-1]=='(':
            stack.pop()
            answer +=len(stack)
        elif x == ')':
            stack.pop()
            answer += 1
    return answer

arrangement = "()(((()())(())()))(())"
print(solution(arrangement))