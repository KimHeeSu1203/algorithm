
def countwrong(word1, words, visit):
    onewrong = []

    for word2 in words:
        tmp_count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                tmp_count += 1

        if (tmp_count == 1) & (word2 not in visit):
            onewrong.append(word2)

    return onewrong



def solution(begin, target, words):
    stack = []
    visit = []
    answer = 0

    def dfs(start):
        tmp_stack = [start]
        while(tmp_stack):
            num = tmp_stack.pop()
            tmp_stack.append(countwrong(num,words,visit))


    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]