def check(words1,words2):
    count = 0
    len = len(words1)
    for i in range(len):
        if words1[i]!=words2[i]:
            count += 1
    return count
def dfs(begin,target,words,visit):
    # 차이 1밖에 안되는 애들 다시 리스트에 넣어서 쭉 만들어보는 것 해야하는가


def solution(begin, target, words):
    answer = 0
    visit = [0]*len(words)
    #visit[words.insert(begin)] == 1
    start = 0

    for i in range()
    """
    while 0 in visit:
        if visit[start]==0:
            dfs(begin,target,words,visit)
        start += 1
    """
    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))