#최댓값을, 둘째 줄에는 최솟값을 출력한다
#식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다.
#덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)
answer = []

def DFS(n, i, numlist, symlist, tmp_answer):
    global answer
    if (len(tmp_answer) == (2*int(n)-1)): #조건 다시 보기
        answer.append(tmp_answer)
        print(answer)
        return
    else: #기호랑 숫자 하나씩 더 붙일
        for k in range(len(symlist)):
            tmp_answer.append(symlist[k])
            tmp_answer.append(numlist[0])
            DFS(n,i+1,numlist[i+1:],symlist[:k]+symlist[k+1:],tmp_answer)
            tmp_answer.pop()
            tmp_answer.pop()


def solution():
    global answer
    n = input()
    numlist = input().split(' ')
    tmp_symlist = input().split(' ')
    symlist = []
    if tmp_symlist[0] != '0' :
        symlist.append(int(tmp_symlist[0])*'+')
    if tmp_symlist[1] != '0' :
        symlist.append(int(tmp_symlist[1])*'-')
    if tmp_symlist[2] != '0' :
        symlist.append(int(tmp_symlist[2])*'*')
    if tmp_symlist[3] != '0' :
        symlist.append(int(tmp_symlist[3])*'/')
    tmp_answer = [numlist[0]]

    DFS(n,0,numlist[1:],symlist,tmp_answer)# 0은 현재 길이



solution()