def dfs(begin,target,answer,words):
    global prevans
    if begin == target:
        if len(answer) < prevans:
            print("답", begin,target)
            prevans = len(answer)
            return

    one_diff = []

    for tmp_word in words:
        print(tmp_word)
        tmp_wrong = 0
        for k in range(len(tmp_word)):
            if tmp_word[k] != begin[k]:
                tmp_wrong += 1
        if (tmp_wrong == 1) & (tmp_word not in answer):
            one_diff.append(tmp_word)

    for diff in one_diff:
        dfs(diff,target,answer.append(diff),words)


def solution(begin, target, words):
    global prevans
    prevans= 1000
    if target not in words:
        return 0
    else:
        answer = []
        dfs(begin,target,answer,words)
    return prevans


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin,target,words))