def solution(numbers):
    answer = ''
    num_Array = []
    for i in range(len(numbers)):
        num = i, str(numbers[i])[0]
        num_Array.append(num)
        num_Array.sort(key=lambda x:(x[1],x[0]),reverse=True)

    print(num_Array)
    for i in range(len(num_Array)):
        x = num_Array[i][0]
        answer += str(numbers[x])
    return answer


numbers = [3, 30, 34, 5, 9]
print(solution(numbers))