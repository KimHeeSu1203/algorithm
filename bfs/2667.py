"""
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우,
혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
"""

import queue

q = queue.Queue()
N = int(input())
apartLine = list()
tmp_zero = [0 for col in range(N)]
print(tmp_zero)
apartLine.append(tmp_zero)
for i in range(N):
    apartLine.append(input()) # 7번 넣고
apartLine.append(tmp_zero)

"""
for i in range(N):
    apartLine[i].insert(8,0)
    apartLine[i].insert(0,0)
"""

print(apartLine)

for i in range(N):
    for j in range(N):
        if apartLine[i][j] == 1:
            q.put()