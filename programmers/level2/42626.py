def solution_1(scoville, K):
    tmp_scoville = sorted(scoville, reverse=True)

    for i in range(len(tmp_scoville) - 2, -1, -1):
        tmp_scoville[i] = tmp_scoville[i + 1] + (tmp_scoville[i] * 2)
        tmp_scoville.pop(-1)
        tmp_scoville = sorted(tmp_scoville, reverse=True)
        if tmp_scoville[-1] > K:
            return len(scoville)-1-i

    return -1

def solution(scoville, K):
    tmp_scoville = sorted(scoville, reverse=True)

    for i in range(len(tmp_scoville) - 2, -1, -1):
        tmp_scoville[i] = tmp_scoville[i + 1] + (tmp_scoville[i] * 2)
        tmp_scoville.pop(-1)

        tmp_scoville = sorted(tmp_scoville, reverse=True)
        if tmp_scoville[-1] > K:
            return len(scoville)-1-i

    return -1

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville,K))