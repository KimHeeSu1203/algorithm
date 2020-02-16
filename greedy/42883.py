def solution(number, k):
    answer = ''
    number = list(str(number))
    stack = []
    stack.append(number[0])
    for i in range(1,len(number)):
        stack.append(number[i])
        print("stack", stack)
        size = len(stack)-1
        if(stack[size-1]<stack[size]) & (k>=0):
            stack.pop(i-1)
            k -= 1
            print("k",k)
            print("stack", stack)

    answer = "".join(stack)[:-k]
    return answer

number = int(input())
k = int(input())
print(solution(number,k))


