def solution(n):
    soobak = '수박'
    answer = []
    n_answer = n // 2

    for i in range(n_answer):
        answer.append(soobak)

    if n % 2 == 1:
        answer.append('수')


    return "".join(answer)

n = 3
print(solution(n))