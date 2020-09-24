def makeCand(brown,yellow):
    sumBY = brown + yellow
    answer = []
    for i in range(3, sumBY):
        if ((sumBY//i) == (sumBY/i)) & ((sumBY//i) >= 3) & ((sumBY//i) <= i):
            answer.append([i,sumBY//i])
    return answer

def solution(brown, yellow):
    candidate = makeCand(brown,yellow)
    for i in range(len(candidate)):
        a,b = candidate[i]
        if (((a-2)*(b-2)) == yellow) & ((a*b - yellow) == brown):
            answer = [a,b]
    return answer


brown = 24
yellow = 24
print(solution(brown,yellow))