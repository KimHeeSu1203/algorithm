def solution(number, k):
    answer = ''
    number = list(str(number))

    for _ in range(k):
        n_index = number.index(sorted(number)[0])
        number.pop(n_index)
    answer = "".join(number)
    return answer


number = int(input())
k = int(input())
print(solution(number,k))


