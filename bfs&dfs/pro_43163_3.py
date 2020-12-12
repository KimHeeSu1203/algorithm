answer = []

def dfs(begin,target,words,tmp_answer):
    if begin == target:
        answer.append(tmp_answer)
        return
    diff = []
    for word in words:
        diffCount = 0
        for i in range(len(word)):
            if word[i] != begin[i]:
                diffCount += 1

        if (diffCount == 1) & (word not in tmp_answer):
            diff.append(word)

    for word in diff:
        tmpList = tmp_answer.copy()
        tmpList.append(word)
        dfs(word, target,words, tmpList)

def solution(begin, target, words):
    if target not in words:
        return 0
    dfs(begin,target,words,[])
    return len(min(answer))


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin,target,words))
