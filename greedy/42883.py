def solution(number, k):
    answer = ''
    number = list(str(number))
    stack = []
    ans_len = len(number)-k
    for i in range(ans_len):
        stack.append(number[i])
    print(stack)
    for i in range(ans_len,len(number)):
        if(number[i]>=min(stack)):
            stack.pop(stack.index(min(stack)))
            stack.append(number[i])
            print("stack : ", stack)
    answer = "".join(stack)
    return answer

number = 4177252841
k = 4
print(solution(number,k))


## 이건 앞에부터 빼는게 안되니까 이렇게 풀면 안된다. 