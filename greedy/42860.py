"""
커밋 수정 2020. 02. 18 아직 풀지 못함
"""

def solution(name):
    answer = 0
    len_name=len(name)
    init="A"*len_name
    chk=[]
    ## Number of movements
    for i in range(len_name):
        if ord(name[i]) == 65:
            pass
        else:
            tmp=ord(name[i]) - 65
            chk.append(i)
            if tmp>13:
                answer+=26-tmp
            else:
                answer+=tmp
    ind=0

    ## Greedy algorithm
    while chk!=[]:
        tmp1=min(abs(chk[0]-ind),len_name-abs(chk[0]-ind))
        tmp2=min(abs(chk[-1]-ind),len_name-abs(chk[-1]-ind))
        min_chk=min(tmp1,tmp2)
        #print("tmp1:{}\ttmp2:{}".format(tmp1,tmp2))
        if tmp1>tmp2:
            ind=chk.pop()
            answer+=tmp2
        else :
            ind=chk.pop(0)
            answer+=tmp1
        #print("ind:{}\tchk:{}".format(ind,chk))
    return answer

print(solution("BBAAAABAABA"))