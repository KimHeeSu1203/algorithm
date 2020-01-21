

"""

차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에,
한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다.
특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다.

(한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있다고 간주한다)

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면
총 몇 마리의 지렁이가 필요한지 알 수 있다.

예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.

(0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.)
"""


def bfs(M,N,ground,visit):
    count = 0
    q = []
    for i in range(N):#8
        for j in range(M): #10
            if (ground[i][j] == 1) & (visit[i][j]==0):
                q.append([i,j])
                while q:
                    [a,b] = q.pop(0)
                    visit[b][a]=1

                        next_XY = XY(next_X, next_Y)
                        if (next_X < 0 | next_X > len(ground)-1| next_Y < 0 | next_Y > len(ground[0])-1 | visit[next_X][next_Y]== 1):
                            print("next_X",next_X)
                            print("next_Y",next_Y)
                            continue
                        q.append(next_XY)
                count += 1
    print("count")
    print(count)


caseNum = int(input())

for i in range(caseNum):

    M,N,K = map(int,input().split())
    ground = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]

    for j in range(K):
        x, y = map(int,input().split())
        ground[y][x] = 1

    bfs(M,N,ground,visit)
    """
    size_x, size_y, K = map(int,input().split()) #가로, 세
    ground=[[0 for col in range(size_x)] for row in range(size_y)] # ground 만들고
    print("ground")
    print(ground)
    visit = [[0 for col in range(size_x)] for row in range(size_y)]
    for j in range(K):
        x,y = map(int,input().split())
        ground[y][x]=1
    bfs(ground,visit)

"""



"""
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
"""