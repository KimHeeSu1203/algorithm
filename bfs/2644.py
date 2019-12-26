"""
사람들은 1, 2, 3, …, n (1≤n≤100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다.
그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

각 사람의 부모는 최대 한 명만 주어진다.

입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.
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

visit = []
family_size = []
for i in range (1,personNum+1):
    if (i in visit)  : # 이미 들렸던지 자식이 없는 노드면 안보고 넘어간다
        continue
    elif (len(all[i].childs)==0):
        continue

    q = [] # 노드를 의미
    q.append(all[i])
    visit.append(i)

    k = 0
    while q:
        node = q.pop(0)
        for j in range(len(node.childs)):
            q.append(all[node.childs[j]])
            k+=1
        visit.extend(node.childs)

    family_size.append(k)

if :다른 집안 가족일 경우 -1
if visit.index(getPerson1) > visit.index(getPerson2) : # person1이 어른일 경우

print("visit")
print(visit)
print("family")
print(family_size)

"""
q = []
visited = set()
while q :
    node = q.pop(0) # 탐색 할 애 뺸다
    if node in visited:
        continue
    q.extend(node.childs)

"""


