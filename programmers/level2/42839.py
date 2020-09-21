from itertools import permutations

def makeSum(allList):
    count = 0
    for i in range(len(allList)):
        flag = True
        for j in range(2,allList[i]):
            if (allList[i]/j) == (allList[i]//j):
                flag = False
                break
        if flag == True:
            count += 1

    return count


def solution(numbers):
    numberList = list(numbers)
    allList = []

    for i in range(1,len(numberList)+1):
        tmpNum = list(map(''.join,permutations(numberList,i)))
        allList += tmpNum

    for i in range(len(allList)):
        allList[i] = int(allList[i])

    allList = sorted(list(set(allList)))
    if 0 in allList:
        allList.pop(0)

    if 1 in allList:
        allList.pop(0)
    answer = makeSum(allList)
    return answer

numbers = "17"
print(solution(numbers))