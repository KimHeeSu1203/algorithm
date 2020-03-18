from itertools import product

def solution(numbers, target):
    answer = 0
    num_list = [(x,-x) for x in numbers]
    final = list(product(*num_list))

    for x in final:
        if sum(x) == target:
            answer += 1
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers,target))