"""
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW

"""
"""
def search(N,M,island): # 같은 아이슬란드를 묶어야 함
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    queue = []
    visit = [[False] * M for _ in range(N)]
    eachIsland = []
    for i in range(N):
        for j in range(M):
            if (island[i][j]=='L') and (not visit[i][j]):
                temp_queue = []
                queue.append([i,j])
                temp_queue.append([i,j])
                visit[i][j] = True
                while queue:
                    _x,_y = queue.pop(0)
                    for k in range(4):
                        nx = _x+dx[k]
                        ny = _y+dy[k]
                        if (0<=nx<N) and (0<=ny<M) and (not visit[nx][ny]) and (island[nx][ny]=='L'):
                            queue.append([nx,ny])
                            visit[nx][ny] = True
                            temp_queue.append([nx, ny])

                eachIsland.append(temp_queue)
    return eachIsland

def distance(N,M,eachIsland):
    for i in range(len(eachIsland)):
        
"""

def findMax(N,list):
    for l in range(N):
        list[l].sort()
        list[l].reverse()
    list.sort()
    list.reverse()
    return list[0][0]

def search(N,M,island):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    queue = []
    count = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if(island[i][j]=='L'):
                visit = [[False] * M for _ in range(N)]
                visit[i][j] = True
                queue.append([i,j])
                tmp_count = [[0] * M for _ in range(N)]
                while queue:
                    _x,_y = queue.pop(0)
                    for k in range(4):
                        nx = _x + dx[k]
                        ny = _y + dy[k]
                        if(0<=nx<N) and (0<=ny<M) and (not visit[nx][ny]) and island[nx][ny]=='L' :
                            tmp_count[nx][ny] = tmp_count[_x][_y] + 1
                            visit[nx][ny] = True
                            queue.append([nx,ny])
                count[i][j] = findMax(N,tmp_count)
    return count

N,M = map(int,input().split()) # 세로 가로
island = []

for i in range(N):
    oneLine = input()
    island.append(oneLine)

result_map = search(N,M,island)
print(findMax(N,result_map))