## combination 말고 다른 방법

def solution(d,budget):
    max = 0
    d.sort()
    for i in range(len(d)):
        if (sum(d[:i+1])) <= budget:
            max = max + 1
        else:
            break
    return max

d = [1,3,2,5,4]
budget = 9
print(solution(d,budget))



""""
from itertools import combinations

def solution(d, budget):
    max = 0
    budget_count = 0
    for i in range(len(d),-1,-1):
        find = list(map(sum,combinations(d,i)))

        for j in find:
            if (j==budget) & (j>max):
                max = j
                budget_count = i
                break
            elif (j<=budget) & (j>max):
                max = j
                budget_count = i

    return budget_count
"""