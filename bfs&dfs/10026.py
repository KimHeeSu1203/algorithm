"""
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다.
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

"""

def bfs(size,box):
    count = 0
    box_visit = [[0 for col in range(size)] for row in range(size)]
    for i in range(size):
        for j in range(size):
            if box_visit[i][j] == 0: # 이미 들린 경우 배제
                q_x = []
                q_y = []
                q_x.append(i)
                q_y.append(j)
                count += 1
                while (len(q_x) > 0) & (len(q_y) > 0): #q가 있을 떄
                    node_x = int(q_x.pop(0))
                    node_y = int(q_y.pop(0))
                    if (node_x != 0):
                        if (box[node_x][node_y] == box[node_x-1][node_y]) & (box_visit[node_x-1][node_y]==0):
                            q_x.append(node_x-1)
                            q_y.append(node_y)
                            box_visit[node_x - 1][node_y] =1

                    if (node_x != size-1):
                        if (box[node_x][node_y] == box[node_x+1][node_y]) & (box_visit[node_x+1][node_y]==0):
                            q_x.append(node_x +1)
                            q_y.append(node_y)
                            box_visit[node_x+1][node_y]=1

                    if (node_y != 0):
                        if(box[node_x][node_y] == box[node_x][node_y-1]) & (box_visit[node_x][node_y-1]==0):
                            q_x.append(node_x)
                            q_y.append(node_y-1)
                            box_visit[node_x][node_y-1]=1

                    if (node_y != size-1):
                        if(box[node_x][node_y] == box[node_x][node_y+1]) & (box_visit[node_x][node_y+1]==0):
                            q_x.append(node_x)
                            q_y.append(node_y+1)
                            box_visit[node_x][node_y + 1]=1


    return count



size = int(input())
box_origin = []
for i in range(size):
    tmp_box = input()
    box_origin.append(tmp_box)

box_jeok = []

for i in range(size):
    temp_jeok = []
    for j in range(size):
        if box_origin[i][j] == 'G':
            temp_jeok.append('R')
        else:
            temp_jeok.append(box_origin[i][j])
    box_jeok.append(temp_jeok)

a = bfs(size,box_origin)
b = bfs(size,box_jeok)

print(a,b)