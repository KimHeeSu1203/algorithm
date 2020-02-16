def solution(number, k):
    answer = ''
    number = list(str(number))
    stack = []
    stack.append(number[0])
    m = 0
    for i in range(1,len(number)):
        stack.append(number[i])
        size = len(stack)-1
        print("m1",m)
        print("stack", stack)
        if(stack[size-1]<stack[size-2]) & (m!=k):
            stack.pop(size-1)
            print(stack)
            m += 1
            print("m2", m)

    answer = "".join(stack)[:-k]
    return answer

number = int(input())
k = int(input())
print(solution(number,k))


