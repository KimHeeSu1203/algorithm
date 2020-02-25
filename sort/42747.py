def solution(citations):
    length = len(citations)
    blink = [0 for _ in range(length)]

    for i in range(len(citations),-1,-1):
        print("i",i)
        answer = 0
        for tmp in citations:
            if tmp >= i:
                answer += 1
        if answer >= i :
            return i


citations = [3, 0, 6, 3, 5]
print(solution(citations))