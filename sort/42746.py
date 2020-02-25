def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    answer = "".join(sorted(numbers,key=lambda x:(x[0],x[1%len(x)],x[2%len(x)],x[3%len(x)]),reverse=True))
    if int(answer) != 0:
        return answer
    else:
        return "0"


numbers = [3, 30, 34, 5, 9]
print(solution(numbers))