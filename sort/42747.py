def solution(citations):
    length = len(citations)
    blink = [0 for _ in range(length)]

    for i in citations:
        answer = 0
        for j in citations:
            if (i<=j):
                answer += 1
        if answer == i:
            return answer

citations = [3, 0, 6, 1, 5]
print(solution(citations))