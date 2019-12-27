"""
사람들은 1, 2, 3, …, n (1≤n≤100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다.
그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

각 사람의 부모는 최대 한 명만 주어진다.

입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.
"""


"""
양방향성을 고려하지 않아서인가 잘못풀었음 
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.childs = []

    def childAppend(self, child):
        self.childs.append(child)

all = list()

personNum = int(input())
getPerson1, getPerson2 = map(int,input().split())
getChon = int(input())

# 전체를 담을 틀을 만들었음 숫자 맞추려고 +1 했
for i in range(personNum+1):
    tmp_n = Node(i)
    all.append(tmp_n)

for i in range(getChon):
    mom, child = map(int,input().split())
    all[mom].childAppend(child)


visit_person=[]
visit_chon = [0 for i in range(personNum+1)]
family_size = [0]

k = 1
for i in range (1,personNum+1):
    if (i in visit_person) | (len(all[i].childs)==0): # 이미 들렸던지 자식이 없는 노드면 안보고 넘어간다
        k+=1
        continue

    q = [] # 노드를 의미
    q.append(all[i])
    visit_person.append(i)
    temp_chon=0
    while q:
        temp_chon += 1
        node = q.pop(0)
        k += len(node.childs)
        for j in range(len(node.childs)):
            q.append(all[node.childs[j]])
            visit_chon[node.childs[j]]=temp_chon
        visit_person.extend(node.childs)
    family_size.append(k)




#다른 집안 가족일 경우 -1

for i in range(len(family_size)-1):
    group = visit_person[family_size[i]:family_size[i+1]]
    if (getPerson1 in group) & (getPerson2 in group):
        if visit_person.index(getPerson1) < visit_person.index(getPerson2): # person1이 어른일 경우
            chon = visit_chon[getPerson2]+visit_chon[getPerson1]
            print(chon)

        elif visit_person.index(getPerson1) > visit_person.index(getPerson2):
            chon = visit_chon[getPerson1]>visit_chon[getPerson2]
            print(chon)
        break

    else:
        print("-1")
        break



