# 프로그래머스42584
def solution(prices):
    answer = []
    for i in range(len(prices)):
        stack = []
        for j in range(i+1,len(prices)):
            if prices[j]>=prices[i]:
                stack.append(j)
            else:
                stack.append(j)
                break
        answer.append(len(stack))
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))